FROM php:7.4-fpm

MAINTAINER Olivier RICARD <olivier.docker@talkspirit.com>

RUN apt-get update

RUN apt-get install -y  libzip-dev zlib1g-dev libpq-dev git libicu-dev libxml2-dev \
    && docker-php-ext-configure intl \
    && docker-php-ext-install intl \
    && docker-php-ext-install pdo mysqli pdo_mysql \
    && docker-php-ext-install zip xml

# Set timezone
RUN rm /etc/localtime
RUN ln -s /usr/share/zoneinfo/Europe/Paris /etc/localtime
RUN "date"

WORKDIR /var/www/
