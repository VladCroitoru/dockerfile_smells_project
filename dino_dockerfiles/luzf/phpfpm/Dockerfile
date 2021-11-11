FROM php:7.1-fpm

RUN docker-php-ext-install pdo pdo_mysql opcache

RUN apt-get update \
    && apt-get install -y libicu-dev libfreetype6-dev libjpeg62-turbo-dev libpng12-dev git

RUN pecl install redis-3.0.0 \
    && docker-php-ext-enable redis

RUN docker-php-ext-install intl

RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN docker-php-ext-install zip

RUN usermod -u 1000 www-data

WORKDIR /var/www