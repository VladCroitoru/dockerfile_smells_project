FROM ubuntu:latest
MAINTAINER winya <winyaa@gmail.com>

RUN apt-get update && \
	apt-get -y upgrade && \
	DEBIAN_FRONTEND=noninteractive apt-get install -y \
		apache2 \
		libapache2-mod-php5 \
		libapache2-mod-rpaf \
		php5 \
		php5-cli \
		php5-dev \
		php5-gd \
		php5-imagick \
		php5-mcrypt \
		php5-memcache \
		php5-mysql 

RUN a2enmod php5
RUN a2enmod rewrite

RUN sed -i "s/short_open_tag = Off/short_open_tag = On/" /etc/php5/apache2/php.ini
RUN sed -i "s/error_reporting = .*$/error_reporting = E_ERROR | E_WARNING | E_PARSE/" /etc/php5/apache2/php.ini

env APACHE_RUN_USER    www-data
env APACHE_RUN_GROUP   www-data
env APACHE_PID_FILE    /var/run/apache2.pid
env APACHE_RUN_DIR     /var/run/apache2
env APACHE_LOCK_DIR    /var/lock/apache2
env APACHE_LOG_DIR     /var/log/apache2
env LANG               C

EXPOSE 80

CMD /usr/sbin/apache2ctl -D FOREGROUND