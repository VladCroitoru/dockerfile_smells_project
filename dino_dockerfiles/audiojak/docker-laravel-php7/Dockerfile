FROM php:7-apache

RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
    && docker-php-ext-install -j$(nproc) iconv mcrypt \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd \
    && docker-php-ext-install pdo pdo_mysql mysqli

RUN a2enmod rewrite

RUN sed -i 's#DocumentRoot /var/www/html#DocumentRoot /var/www/laravel/laravel/public#' /etc/apache2/apache2.conf
RUN sed -i 's#Listen 80#Listen 8080#' /etc/apache2/apache2.conf

EXPOSE 8080

MAINTAINER John Kennedy
