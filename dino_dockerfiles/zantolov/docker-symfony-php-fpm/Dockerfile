FROM php:7.3-fpm

RUN apt-get update && apt-get install -y \
    git \
    unzip

RUN apt-get install -y libzip-dev zlib1g-dev libicu-dev g++
RUN docker-php-ext-configure intl
RUN docker-php-ext-install intl

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN docker-php-ext-install pdo
RUN docker-php-ext-install opcache
RUN docker-php-ext-install zip
RUN docker-php-ext-install intl

RUN apt-get install -y libpq-dev
RUN docker-php-ext-install pdo_pgsql

ADD custom.ini /usr/local/etc/php/conf.d/custom.ini

RUN useradd -m symfony
USER symfony

RUN composer --version

WORKDIR /var/www/symfony
