FROM php:7.0.21-alpine

COPY php.ini /usr/local/etc/php/

# System dependencies
RUN apk upgrade --update && apk add libmcrypt-dev postgresql-dev autoconf g++ make pcre-dev icu-dev > /dev/null

# PHP dependencies
RUN docker-php-ext-install pdo mcrypt pdo_pgsql intl > /dev/null

# Install mongodb extension
RUN \
    apk add --no-cache --virtual .mongodb-ext-build-deps openssl-dev && \
    pecl install mongodb > /dev/null 2> /dev/null && \
    pecl clear-cache && \
    apk del .mongodb-ext-build-deps && \
    docker-php-ext-enable mongodb.so

# Install imagick extension
RUN apk add --no-cache imagemagick imagemagick-dev libtool && \
    pecl install imagick-3.4.3 > /dev/null 2> /dev/null && \
    docker-php-ext-enable imagick


# Install phpunit
COPY phpunit.phar /
RUN chmod +x /phpunit.phar
