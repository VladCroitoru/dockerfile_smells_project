FROM php:7.4-apache

RUN apt-get update && apt-get install -y build-essential libssl-dev zlib1g-dev libpng-dev libjpeg-dev libfreetype6-dev

RUN docker-php-ext-install pdo pdo_mysql mysqli gd
