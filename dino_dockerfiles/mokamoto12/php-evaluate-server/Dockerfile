FROM composer:1.5.5 AS build

COPY composer.json composer.lock /app/

RUN composer install

FROM php:7.1.12-apache-jessie

COPY --from=build /app/vendor /var/www/vendor/

COPY . /var/www/

RUN ln -s /var/www/public/* /var/www/html/
