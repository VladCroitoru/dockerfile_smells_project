# Dockerfile for rastermedia/laravel-docker based on Homestead nginx + php-fpm
FROM ubuntu:14.04

# Update and install dependencies
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install php5 php5-cli php5-mcrypt php5-gd php5-json php5-mysql php5-memcached apache2 libapache2-mod-php5 curl php5-curl git-core 
RUN rm /etc/apache2/sites-*/*
RUN php5enmod mcrypt
RUN a2enmod rewrite
ADD ./apache.vhost.conf /etc/apache2/sites-enabled/laravel.conf

# Grab composer and install it in /usr/local/bin/composer
RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer

ADD ./start.sh /start.sh

VOLUME /var/www/laravel
VOLUME /var/log

CMD ["/start.sh"]
