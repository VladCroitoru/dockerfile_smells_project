# 
# PHP With required extension and composer to build and test Laravel App on CI / Gitlab CI
#

FROM php:5.6

MAINTAINER Sucipto <chip@pringstudio.com>

RUN apt-get update -yqq
RUN apt-get install git libcurl4-gnutls-dev libicu-dev libmcrypt-dev libvpx-dev libjpeg-dev libpng-dev libxpm-dev zlib1g-dev libfreetype6-dev libxml2-dev libexpat1-dev libbz2-dev libgmp3-dev libldap2-dev unixodbc-dev libpq-dev libsqlite3-dev libaspell-dev libsnmp-dev libpcre3-dev libtidy-dev -yqq
RUN docker-php-ext-install mbstring mcrypt pdo_mysql curl json intl gd xml zip bz2 opcache mysql
RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/bin/composer
