
# Node.js + Socket.io + PHP 7.1 + composer
FROM phusion/baseimage:latest

LABEL maintainer "Doitmagic <razvan@doitmagic.com>"

ENV COMPOSER_VERSION=1.6.5
RUN LC_ALL=C.UTF-8 add-apt-repository -y ppa:ondrej/php

RUN mkdir -p /var/www
RUN mkdir -p /var/script

#Install php + composer
RUN apt-get update -qq && apt-get install --no-install-recommends -y \
    php7.1-cli \
    php7.1-fpm \
    php7.1-curl \
    php7.1-json \
    php7.1-mysql \
    php7.1-mcrypt \
    php7.1-soap \
    php7.1-mbstring \
    php7.1-xml \
    php7.1-bcmath \
    php7.1-zip \
    php7.1-imap \
    php7.1-intl \
    php-xdebug \
    php-apcu php-apcu-bc \
    php-imagick php-memcache \
    git \
    && phpdismod xdebug \
    && ln -s /etc/php/7.1 /etc/php/current \
    && apt-get clean autoclean \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY php-fpm.sh /etc/service/php-fpm/run

# configure php
COPY php/fpm/ /etc/php/7.1/fpm/
COPY php/php-cli.ini /etc/php/7.1/cli/php.ini
RUN mkdir /var/log/fpm && chown www-data:www-data /var/log/fpm

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer

#install node 6.X + socket.io
RUN curl -sL https://deb.nodesource.com/setup_8.x |  bash -

RUN apt-get update && apt-get install -y nodejs
RUN apt-get install  -y python  build-essential
ADD package.json /var/package.json



RUN npm install express && npm install socket.io && npm install redis &&  npm install mysql && npm install request

VOLUME [/var/www,/var/script,/var/package.json]

WORKDIR /var/script

EXPOSE 3500/tcp 6379

CMD "/bin/sh" "-c" "node index.js"
