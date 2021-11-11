FROM php:7.2-apache

ENV TERM xterm-256color

ARG NODE_VERSION=12
ARG BOLT_VERSION=3.7

RUN apt-get update && apt-get install -y \
    libpq-dev \
    libpng-dev \
    libjpeg62-turbo-dev \
    libfreetype6-dev \
    libxrender1 \
    libfontconfig1 \
    libicu-dev \
    wget\
    nano

RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd pdo_mysql exif zip \
    && apt-get clean && rm -rf /var/lib/apt/lists/* \
    && docker-php-ext-configure intl \
    && docker-php-ext-install intl

RUN a2enmod headers && a2enmod rewrite

COPY ./apache-bolt.conf /etc/apache2/sites-available/000-default.conf
COPY ./extra-php-config.ini /usr/local/etc/php/conf.d

RUN curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer \
    && composer self-update \
    && composer global require hirak/prestissimo

RUN curl -sL https://deb.nodesource.com/setup_${NODE_VERSION}.x | bash - \
    && apt-get install -y nodejs

WORKDIR /var/www

RUN rm -rf html && composer create-project bolt/composer-install:^${BOLT_VERSION} html --prefer-dist --no-interaction

WORKDIR /var/www/html

RUN chown -R www-data:www-data /var/www/html
