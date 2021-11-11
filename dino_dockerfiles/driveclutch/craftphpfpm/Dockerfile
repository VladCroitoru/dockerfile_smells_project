FROM php:7.0.12-fpm

MAINTAINER David Hallum <david@driveclutch.com>

RUN apt-get update -q \
    && apt-get --no-install-recommends --no-install-suggests -y install \
      libfreetype6-dev \
      libjpeg62-turbo-dev \
      libmagickwand-dev \
      libmcrypt-dev \
      libpng12-dev \
      libcurl4-nss-dev \
    && pecl install imagick \
    && docker-php-ext-install mcrypt \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd \
    && docker-php-ext-install curl \
    && docker-php-ext-install pdo \
    && docker-php-ext-install pdo_mysql \
    && docker-php-ext-install json \
    && docker-php-ext-enable imagick

