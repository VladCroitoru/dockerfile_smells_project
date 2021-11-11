FROM php:7-apache

MAINTAINER Donovan Tengblad

RUN a2enmod rewrite

RUN apt-get update && apt-get install -y \
  vim \
  unzip \
  zip \
  xz-utils \
  zlib1g-dev \
  libcurl4-gnutls-dev \
  git \
  curl

RUN docker-php-ext-install pdo pdo_mysql curl zip

RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer

COPY ./api.conf /etc/apache2/sites-available/api.conf

RUN a2dissite 000-default && a2ensite api.conf

RUN a2enmod proxy && a2enmod proxy_http

COPY ./php.ini /usr/local/etc/php/ 

CMD ["apache2-foreground"]
