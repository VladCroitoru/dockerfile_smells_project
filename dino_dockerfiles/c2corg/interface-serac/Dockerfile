FROM php:7.1-apache

ENV DEBIAN_FRONTEND noninteractive

RUN echo 'APT::Install-Recommends "0";' > /etc/apt/apt.conf.d/50no-install-recommends
RUN echo 'APT::Install-Suggests "0";' > /etc/apt/apt.conf.d/50no-install-suggests

RUN a2enmod rewrite
RUN apt-get update \
 && apt-get -y install libpq5 libpq-dev \
 && docker-php-ext-install pdo pdo_pgsql \
 && apt-get -y purge --auto-remove libpq-dev \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

COPY class/ /var/www/class/
COPY lib/ /var/www/lib/
COPY partials/ /var/www/partials/
COPY www/* /var/www/html/
