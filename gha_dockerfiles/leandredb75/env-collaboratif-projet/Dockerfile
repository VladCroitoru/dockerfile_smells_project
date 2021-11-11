FROM php:8.0-apache

ENV COMPOSER_ALLOW_SUPERUSER=1
WORKDIR /var/www/html
ADD . .

RUN apt-get update -qq && \
    apt-get install -qy \
    git \
    gnupg \
    unzip \
    zip 
RUN docker-php-ext-install -j$(nproc) opcache pdo_mysql
RUN apt-get update && apt-get install -y libzip-dev zip libmemcached-dev\
    && pecl install memcached\
    && docker-php-ext-enable memcached

ADD ./server/vhost.conf /etc/apache2/sites-available/000-default.conf
ADD ./server/apache.conf /etc/apache2/conf-available/z-app.conf
ADD ./server/php.ini /usr/local/etc/php/conf.d/php.ini

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer