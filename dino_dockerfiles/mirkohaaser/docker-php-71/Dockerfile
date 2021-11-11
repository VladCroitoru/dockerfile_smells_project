FROM php:7.1-fpm

MAINTAINER Mirko Haaser <kontakt@mirko-haaser.de>

# Common tools needed later
RUN apt-get update
RUN apt-get install -y openssl git

# Install image extensions
RUN apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libpng12-dev libgd-dev
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ 
RUN docker-php-ext-install gd exif

# Install database extension
RUN docker-php-ext-install mysqli pdo pdo_mysql

# Install string ectensions
RUN docker-php-ext-install gettext mbstring

# Install mcrypt
RUN apt-get install -y libmcrypt-dev
RUN docker-php-ext-install mcrypt

# Install compression extension
RUN apt-get update 
RUN apt-get install -y libbz2-dev zlib1g-dev 
RUN docker-php-ext-install zip bz2
