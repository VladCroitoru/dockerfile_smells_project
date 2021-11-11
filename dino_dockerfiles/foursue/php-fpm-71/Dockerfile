FROM php:7.1-fpm-alpine
MAINTAINER foursue@gmail.com

# php ext
RUN apk update && \
    apk --no-cache upgrade && \
    apk add libmcrypt-dev mysql-client git
RUN git clone https://github.com/phpredis/phpredis.git /usr/src/php/ext/redis
RUN docker-php-ext-install mcrypt pdo_mysql json mbstring redis

# compser
RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer
RUN composer config -g repos.packagist composer https://packagist.jp
RUN composer global require hirak/prestissimo

