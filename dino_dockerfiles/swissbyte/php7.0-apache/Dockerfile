FROM php:7.0-apache

RUN docker-php-ext-install mysqli

RUN apt-get update -y && apt-get install -y sendmail libpng-dev

RUN apt-get update && \
    apt-get install -y \
        zlib1g-dev 

RUN docker-php-ext-install mbstring

RUN docker-php-ext-install zip

RUN docker-php-ext-install gd

RUN docker-php-ext-install pdo_mysql

RUN a2enmod rewrite

RUN a2enmod headers

RUN a2enmod proxy
