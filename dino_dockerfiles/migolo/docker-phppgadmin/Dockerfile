FROM php:5.5.34-apache

RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
        libbz2-dev \
        git \
        libpq-dev \
        postgresql-contrib \
    && docker-php-ext-install iconv mcrypt \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install bz2 \
    && docker-php-ext-install zip \
    && docker-php-ext-install gd \
    && docker-php-ext-install mbstring \
    && docker-php-ext-install pgsql \
    && docker-php-ext-install pdo_pgsql

RUN a2enmod rewrite
RUN a2enmod headers
RUN a2enmod expires

RUN usermod -u 1000 www-data
RUN cd /var/www/ && git clone git://github.com/phppgadmin/phppgadmin.git ./html
