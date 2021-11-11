FROM php:5.6-apache

RUN apt-get update && apt-get install -y zlib1g-dev libicu-dev libpq-dev php5-mcrypt php5-gd \
	libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
    && docker-php-ext-install -j$(nproc) iconv mcrypt \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd

RUN docker-php-ext-install opcache
RUN docker-php-ext-install intl
RUN docker-php-ext-install pdo_mysql
RUN docker-php-ext-install exif

RUN ["cp", "/etc/apache2/mods-available/rewrite.load", "/etc/apache2/mods-enabled/"]