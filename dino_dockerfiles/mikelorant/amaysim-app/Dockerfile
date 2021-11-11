FROM php:apache

ENV DB_HOST localhost
ENV DB_USER user
ENV DB_PASS password

RUN docker-php-ext-install mysqli

COPY app1/ /var/www/html
