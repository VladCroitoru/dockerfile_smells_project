FROM debian:jessie
MAINTAINER L. Mangani <lorenzo.mangani@gmail.com>
# v.5.x

# Default baseimage settings
ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive

# Update and upgrade apt
RUN apt-get update -qq
# RUN apt-get upgrade -y
RUN apt-get install --no-install-recommends --no-install-suggests -yqq ca-certificates apache2 libapache2-mod-php5 php5 php5-cli php5-gd php-pear php5-dev php5-mysql php5-json php-services-json git wget pwgen curl && rm -rf /var/lib/apt/lists/*
RUN a2enmod php5

# MySQL
RUN groupadd -r mysql && useradd -r -g mysql mysql
RUN mkdir /docker-entrypoint-initdb.d

# Perl + MySQL DBI
RUN apt-get update && apt-get install -y perl libdbi-perl libclass-dbi-mysql-perl --no-install-recommends && rm -rf /var/lib/apt/lists/*

# gpg: key 5072E1F5: public key "MySQL Release Engineering <mysql-build@oss.oracle.com>" imported
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys A4A9406876FCBD3C456770C88C718D3B5072E1F5
ENV MYSQL_MAJOR 5.6
ENV MYSQL_VERSION 5.6.27
RUN echo "deb http://repo.mysql.com/apt/debian/ jessie mysql-${MYSQL_MAJOR}" > /etc/apt/sources.list.d/mysql.list

RUN apt-get update && apt-get install -y mysql-server-5.6 libmysqlclient18 && rm -rf /var/lib/apt/lists/* \
	&& rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql

# comment out a few problematic configuration values
# don't reverse lookup hostnames, they are usually another container
RUN sed -Ei 's/^(bind-address|log)/#&/' /etc/mysql/my.cnf \
	&& echo 'skip-host-cache\nskip-name-resolve' | awk '{ print } $1 == "[mysqld]" && c == 0 { c = 1; system("cat") }' /etc/mysql/my.cnf > /tmp/my.cnf \
	&& mv /tmp/my.cnf /etc/mysql/my.cnf

RUN mkdir -p /var/lib/mysql/
RUN chmod -R 755 /var/lib/mysql/

WORKDIR /

# HOMER 5
RUN git clone --depth 1 https://github.com/sipcapture/homer-api.git /homer-api
RUN git clone --depth 1 https://github.com/sipcapture/homer-ui.git /homer-ui

RUN chmod -R +x /homer-api/scripts/*
RUN cp -R /homer-api/scripts/. /opt/

RUN cp -R /homer-ui/* /var/www/html/
RUN cp -R /homer-api/api /var/www/html/
RUN chown -R www-data:www-data /var/www/html/store/
RUN chmod -R 0775 /var/www/html/store/dashboard

COPY data/configuration.php /var/www/html/api/configuration.php
COPY data/preferences.php /var/www/html/api/preferences.php
COPY data/vhost.conf /etc/apache2/sites-enabled/000-default.conf

# OpenSIPS + sipcapture module
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 049AD65B
RUN echo "deb http://apt.opensips.org jessie 2.2-releases" >>/etc/apt/sources.list
RUN apt-get update -qq && apt-get install -f -yqq rsyslog opensips opensips-geoip-module opensips-json-module opensips-mysql-module opensips-regex-module opensips-restclient-module  && rm -rf /var/lib/apt/lists/*

RUN rm /etc/opensips/opensips.cfg
COPY data/opensips.m4 /etc/opensips/opensips.m4
RUN chmod 775 /etc/opensips/opensips.m4
COPY data/opensips-es.m4 /etc/opensips/opensips-es.m4
RUN chmod 775 /etc/opensips/opensips-es.m4

RUN ln -s /usr/lib64 /usr/lib/x86_64-linux-gnu/

# GeoIP (http://dev.maxmind.com/geoip/legacy/geolite/)
RUN apt-get update -qq && apt-get install -f -yqq geoip-database geoip-database-extra
# RUN cd /usr/share/GeoIP && wget -N -q http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz && gunzip GeoLiteCity.dat.gz

# Install the cron service
RUN touch /var/log/cron.log
RUN apt-get install cron -y

# Add our crontab file
RUN echo "30 3 * * * /opt/homer_rotate >> /var/log/cron.log 2>&1" > /etc/cron.d/homer_rotate.conf
RUN echo "local0.* -/var/log/opensips.log" > /etc/rsyslog.d/opensips.conf

COPY run.sh /run.sh
RUN chmod a+rx /run.sh

COPY data/homer-es-template.json /etc/homer-es-template.json

# Add persistent MySQL volumes
VOLUME ["/etc/mysql", "/var/lib/mysql", "/var/www/html/store"]

# UI
EXPOSE 80
# HEP
EXPOSE 9060

ENTRYPOINT ["/run.sh"]
