FROM php:7.1-fpm

MAINTAINER Brian Winkers <bwinkers@gmail.com>

RUN apt-get update && apt-get install -y \
        git libpq-dev libevent-dev libmcrypt-dev libbz2-dev \
    && docker-php-source extract \
    && docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql \
    && docker-php-ext-install pdo  pdo_mysql pdo_pgsql opcache sockets mcrypt hash bz2 mbstring \
    && pecl install event mongodb \
    && docker-php-ext-enable event mongodb \ 
    && git clone --depth=1 "git://github.com/phalcon/cphalcon.git" \
    && cd cphalcon/build \
    && ./install \
    && docker-php-ext-enable phalcon \
    && docker-php-source delete \
    && cd ../.. \
    && rm -Rf cphalcon

COPY src/ /var/www/html/



