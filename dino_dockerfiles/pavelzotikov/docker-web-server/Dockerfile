FROM ubuntu:14.04
MAINTAINER Pavel Zotikov pavelzotikov@gmail.com

ENV DEBIAN_FRONTEND noninteractive

RUN locale-gen ru_RU.UTF-8 && dpkg-reconfigure locales

RUN apt-get update

RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:ondrej/php
RUN add-apt-repository -y ppa:nginx/stable

RUN sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y nano wget curl libapache2-mod-php5.6 php5.6-mysql php5.6-gd php5.6-curl php-pear php-apc php5.6-mcrypt php5.6-imagick php5.6-memcache php5.6-redis php5.6-mongo supervisor nginx apache2 mysql-server phpmyadmin memcached redis-server mongodb

RUN curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -
RUN apt-get install -y nodejs

# create home dir
# RUN mkdir /var/www/

# nginx config
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf
RUN rm /etc/nginx/sites-enabled/default
ADD nginx.conf /etc/nginx/sites-enabled/default

# apache2 config
# RUN echo "\nServerName 172.17.0.2;" >> /etc/apache2/httpd.conf
RUN rm /etc/apache2/ports.conf
ADD apache2-ports.conf /etc/apache2/ports.conf
RUN rm /etc/apache2/sites-available/000-default.conf
RUN rm /etc/apache2/sites-enabled/000-default.conf
ADD apache2.conf /etc/apache2/sites-enabled/default.conf

# mysql config
RUN echo "\nInclude /etc/phpmyadmin/apache.conf" >> /etc/apache2/apache2.conf
RUN sed -i "s#// \$cfg\['Servers'\]\[\$i\]\['AllowNoPassword'\] = TRUE;#\$cfg\['Servers'\]\[\$i\]\['AllowNoPassword'\] = TRUE;#g" /etc/phpmyadmin/config.inc.php 

# mongodb config
RUN mkdir /var/mongodb

# supervisor config
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf 

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_PID_FILE /var/run/apache2/apache2.pid

RUN a2enmod rewrite

VOLUME ["/var/www"] 

EXPOSE 80 

CMD ["/usr/bin/supervisord"]
