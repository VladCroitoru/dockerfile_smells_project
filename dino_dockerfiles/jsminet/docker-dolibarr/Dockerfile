FROM php:7.4.16-apache-buster
MAINTAINER JS Minet

ENV VERSION 13.0.2

RUN apt-get update && apt-get install -y libpng-dev libjpeg-dev libldap2-dev libicu-dev libzip-dev zip \
    && rm -rf /var/lib/apt/lists/* \
	&& docker-php-ext-install zip \
    && docker-php-ext-configure gd --with-jpeg \
    && docker-php-ext-install gd \
    && docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \
    && docker-php-ext-install ldap \
	&& docker-php-ext-configure intl \
    && docker-php-ext-install intl \
    && docker-php-ext-install mysqli \
    && docker-php-ext-install calendar \
    && apt-get purge -y libpng-dev libjpeg-dev libldap2-dev \
	&& cd /tmp \
    && curl "https://codeload.github.com/Dolibarr/dolibarr/tar.gz/${VERSION}" -o dolibarr.tar.gz \
    && tar -xzf dolibarr.tar.gz \
    && cp -R dolibarr-$VERSION/htdocs/. /var/www/html \
    && rm -R dolibarr-$VERSION \
    && rm dolibarr.tar.gz \
	&& mkdir /var/www/html/documents \
    && chown -hR www-data:www-data /var/www/html

COPY php.ini /usr/local/etc/php

VOLUME ["/var/www/html/conf", "/var/www/html/documents"]

EXPOSE 80
