FROM php:7.0.7-apache

MAINTAINER Donovan Tengblad

RUN a2enmod rewrite

RUN apt-get update && apt-get install -y \
  vim \
  unzip \
  zip \
  xz-utils \
  zlib1g-dev \
  libcurl4-gnutls-dev \
  curl

RUN docker-php-ext-install pdo pdo_mysql curl zip

RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer

COPY ./backend.conf /etc/apache2/sites-available/backend.conf

RUN a2dissite 000-default && a2ensite backend.conf

COPY ./php.ini /usr/local/etc/php/

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["apache2-foreground"]
