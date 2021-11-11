FROM php:7.1-fpm

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y zip unzip

RUN docker-php-ext-install mysqli
