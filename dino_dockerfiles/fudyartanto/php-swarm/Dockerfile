FROM ubuntu:14.04
MAINTAINER arfan@mylits.com

ENV DEBIAN_FRONTEND noninteractive

# install required packages
RUN echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu trusty main" >> /etc/apt/sources.list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-key E5267A6C

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    supervisor \
    apache2 \
    mysql-server \
    php5.6-fpm \
    php5.6-mysql \
    php5.6-gd \
    php5.6-curl \
    php5.6-xml \
    php5.6-mbstring \
    php5.6-zip \
    php7.0-fpm \
    php7.0-mysql \
    php7.0-gd \
    php7.0-curl \
    php7.0-xml \
    php7.0-mbstring \
    php7.0-zip \
  && rm -r /var/lib/apt/lists/*

# configure mysql 
RUN sed -i 's/bind-address/# bind-address/g' /etc/mysql/my.cnf && \
  sed -i 's/^\(log_error\s.*\)/# \1/' /etc/mysql/my.cnf && \
  echo "mysqld_safe &" > /tmp/config && \
  echo "mysqladmin -u root password 'admin' --silent --wait=30 ping || exit 1" >> /tmp/config && \
  echo "mysql -u root -padmin -e 'GRANT ALL PRIVILEGES ON *.* TO \"root\"@\"127.0.0.1\" IDENTIFIED BY \"admin\" WITH GRANT OPTION;'" >> /tmp/config && \
  echo "mysql -u root -padmin -e 'GRANT ALL PRIVILEGES ON *.* TO \"root\"@\"localhost\" IDENTIFIED BY \"admin\" WITH GRANT OPTION;'" >> /tmp/config && \
  echo "mysql -u root -padmin -e 'GRANT ALL PRIVILEGES ON *.* TO \"root\"@\"%\" IDENTIFIED BY \"admin\" WITH GRANT OPTION;'" >> /tmp/config && \
  bash /tmp/config && \
  rm -f /tmp/config

RUN a2enmod proxy
RUN a2enmod proxy_fcgi setenvif
RUN a2enconf php5.6-fpm

RUN mkdir -p /run/php/

# configure apache php5.6-fpm
COPY php5.6-fpm.conf /etc/apache2/conf-available/php5.6-fpm.conf
# RUN ln -s /etc/apache2/conf-available/php5.6-fpm.conf /etc/apache2/conf-enabled/
RUN sed -i 's/\/run\/php\/php5.6-fpm.sock/127.0.0.1:9000/g' /etc/php/5.6/fpm/pool.d/www.conf

# configure apache php7.0-fpm
COPY php7.0-fpm.conf /etc/apache2/conf-available/php7.0-fpm.conf
RUN ln -s /etc/apache2/conf-available/php7.0-fpm.conf /etc/apache2/conf-enabled/
RUN sed -i 's/\/run\/php\/php7.0-fpm.sock/127.0.0.1:9001/g' /etc/php/7.0/fpm/pool.d/www.conf

COPY scripts /scripts
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# install sample dir
RUN mkdir /var/www/html/php5.6
RUN mkdir /var/www/html/php7.0

# add phpinfo
RUN echo "<?php phpinfo();" >> /var/www/html/php5.6/index.php
RUN echo "<?php phpinfo();" >> /var/www/html/php7.0/index.php

RUN mkdir /src
WORKDIR /src

# expose 3306 mysql port
EXPOSE 3306

CMD ["/usr/bin/supervisord"]