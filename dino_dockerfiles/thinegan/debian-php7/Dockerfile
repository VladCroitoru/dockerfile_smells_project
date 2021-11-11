FROM php:7-fpm
MAINTAINER Thinegan Ratnams <thinegan@thinegan.com>

RUN apt-get update && apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libpng-dev mysql-client libicu-dev \
&& docker-php-ext-install gd mysqli