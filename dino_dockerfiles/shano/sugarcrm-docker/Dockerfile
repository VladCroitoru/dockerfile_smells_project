FROM php:5.5-apache

MAINTAINER Ivica Nedeljkovic <ivica.nedeljkovic@gmail.com>

# Dependencies
## Freshen apt's cache so it knows where to find files.
RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y \
        vim \
        wget

## Install gd with it's dependencies
RUN apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
        libc-client-dev \
        libkrb5-dev \
        cron \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd

## Install imap
RUN docker-php-ext-configure imap --with-imap-ssl --with-kerberos \
    && docker-php-ext-install imap

## A few easy to install dependencies
RUN docker-php-ext-install iconv mcrypt json

## Install Zip extension and it's dependencies
RUN apt-get install -y zlib1g zlib1g-dev
RUN docker-php-ext-install zip

## Install Soap extension and it's dependencies
RUN apt-get install -y libxml2 libxml2-dev
RUN docker-php-ext-install simplexml soap

## Install opcache
RUN docker-php-ext-install opcache

## Install mysqli/pdo mysql and it's dependencies
RUN docker-php-ext-install mysqli pdo pdo_mysql

## Install curl extension and it's dependencies
RUN apt-get install -y libcurl3-dev
RUN docker-php-ext-install curl

## Install mbstring
RUN docker-php-ext-install mbstring

## Install exif
RUN docker-php-ext-install exif

## install bcmath
RUN docker-php-ext-install bcmath

# Install XDebug
RUN pecl install -o -f xdebug \
    && rm -rf /tmp/pear
COPY ./docker/config/php/99-xdebug.ini /usr/local/etc/php/conf.d/

# Composer
## Set environment variables
ENV COMPOSER_HOME /root/composer

## Composer expects to have these available
RUN apt-get install -y git

## Install
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

## Apache
COPY ./docker/config/apache/apache2.conf /etc/apache2/

## Enable Apache modules
RUN a2enmod rewrite negotiation headers ssl

# For OSX, maybe need to be removed for other systems???
#RUN usermod -u 1000 www-data

## PHP
COPY ./docker/config/php/php.ini /usr/local/etc/php/

VOLUME ["/app"]

WORKDIR /app

ENV APACHE_RUN_DIR /var/run/apache2

# Copy default cron job
COPY ./docker/config/cron/sugarcrm /etc/cron.d/
RUN chmod 0644 /etc/cron.d/sugarcrm

# Start cron
RUN service cron start

ADD . .

# Setup our site config
RUN rm /etc/apache2/sites-enabled/000-default.conf
COPY ./docker/config/apache/000-default.conf /etc/apache2/sites-enabled/000-default.conf
