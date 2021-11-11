FROM php:5.6-apache

RUN a2enmod rewrite

RUN set -xe \
    && apt-get update \
    && apt-get install -y libpng12-dev libjpeg-dev libmcrypt-dev \
    && rm -rf /var/lib/apt/lists/* \
    && docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
    && docker-php-ext-install gd mcrypt mbstring mysqli zip

WORKDIR /var/www/html
