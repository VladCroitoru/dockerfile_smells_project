FROM php:7.0-apache

MAINTAINER Tom Lomas

RUN a2enmod rewrite

# Install iconv, mcrypt, gd
RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
    && docker-php-ext-install -j$(nproc) iconv mcrypt \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd

## Install PDO, PDO MySQL
RUN docker-php-ext-install -j$(nproc) pdo pdo_mysql

# Install MySQLi (Wordpress support)
RUN docker-php-ext-install -j$(nproc) mysqli
