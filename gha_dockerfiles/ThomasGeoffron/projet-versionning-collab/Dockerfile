FROM php:5.6-fpm-alpine

RUN apk update && \
    apk add php5-mysql && \
    php -r "readfile('http://getcomposer.org/installer');" | php -- --install-dir=/usr/bin/ --filename=composer

RUN docker-php-ext-install pdo mysqli pdo_mysql
    
COPY . .

RUN composer install
