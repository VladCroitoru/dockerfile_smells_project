FROM ubuntu:16.04

RUN apt-get update && apt-get install -y software-properties-common

RUN LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php

RUN apt-get update && apt-get install -y php7.1-fpm php7.1-cli \
    php7.1-json \
    php7.1-xml \
    php7.1-opcache \
    php7.1-mysql \
    php7.1-mbstring \
    php7.1-mcrypt \
    php7.1-zip \
    php7.1-curl \
    php7.1-mysql \
    php-redis \
    php7.1-gmp \
    php7.1-opcache \
    php7.1-bcmath \
    php7.1-gd \
    php-imagick \
    wget curl git unzip

RUN mkdir -p /run/php/ /var/run/php/

COPY install-composer.sh install-composer.sh

RUN chmod +x install-composer.sh

RUN ./install-composer.sh
