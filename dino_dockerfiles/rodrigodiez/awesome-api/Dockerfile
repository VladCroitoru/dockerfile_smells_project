FROM php:7-apache

RUN apt-get update -y
RUN apt-get install -y zlib1g-dev wget

RUN docker-php-ext-install zip pdo_mysql

RUN rm -f /etc/apache2/sites-available/*
RUN rm -f /etc/apache2/sites-enabled/*

COPY awesome-api.conf /etc/apache2/sites-enabled/awesome-api.conf
RUN a2enmod rewrite

COPY . /var/www/html
WORKDIR /var/www/html

RUN chmod +x install-composer.sh
RUN ./install-composer.sh
RUN ./composer.phar install -o --prefer-dist
