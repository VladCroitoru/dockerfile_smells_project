FROM phusion/baseimage:0.9.15

ENV HOME /root
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

WORKDIR /

ENV DB_NAME OBDB
ENV DB_USER admin
ENV DB_PASS obdbpassword
ENV DB_HOST ob-db
ENV TZ_REGION Europe
ENV TZ_CITY Berlin

ENV OB_ADMIN ob_admin
ENV OB_PASS ob_pass

RUN apt-get update && apt-get -y install \
	wget \
	libapache2-mod-php5 \
	php5-cli \
	php5-mysql \
	php5-gd \
	php5-snmp \
	php-pear \
	php5-mcrypt \
	php5-json \
	snmp \
	graphviz \
	subversion \
	mysql-client \
	rrdtool \
	fping \
	imagemagick \
	whois \
	mtr-tiny \
	nmap \
	ipmitool \
	python-mysqldb

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN sed -i "s/\;date\.timezone\ \=/date\.timezone\ \=\ $TZ_REGION\/$TZ_CITY/g" /etc/php5/cli/php.ini && \
	sed -i "s/\;date\.timezone\ \=/date\.timezone\ \=\ $TZ_REGION\/$TZ_CITY/g" /etc/php5/apache2/php.ini

RUN mkdir -p /opt

WORKDIR /opt

RUN wget http://www.observium.org/observium-community-latest.tar.gz \
	&& tar zxvf observium-community-latest.tar.gz \
	&& rm /opt/observium-community-latest.tar.gz \
	&& mkdir observium/logs observium/rrd \
	&& chown www-data:www-data observium/rrd \
	&& rm -fr /var/www/html \
	&& ln -s /opt/observium/html /var/www/html

ADD observium /etc/cron.d/

ADD config.php /opt/observium/

ADD apache.conf /etc/apache2/sites-available/000-default.conf

RUN mkdir /etc/service/apache2
ADD apache2.sh /etc/service/apache2/run

ADD run.sh /

RUN chmod +x /etc/service/apache2/run /run.sh

RUN php5enmod mcrypt \
	&& a2enmod rewrite

WORKDIR /

EXPOSE 80
CMD ["/run.sh"]
