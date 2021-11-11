FROM php:7-alpine

RUN set -xe && \
    apk add --update libmcrypt freetype libpng libjpeg-turbo && \
    apk add --no-cache --virtual .backend-deps libmcrypt-dev freetype-dev libpng-dev libjpeg-turbo-dev && \
    docker-php-ext-configure gd \
        --with-freetype-dir=/usr/include/ \
        --with-png-dir=/usr/include/ \
        --with-jpeg-dir=/usr/include/ && \
    NPROC=$(getconf _NPROCESSORS_ONLN) && \
    docker-php-ext-install pdo_mysql mysqli mcrypt opcache && \
    docker-php-ext-install -j${NPROC} gd && \
    apk del .backend-deps

RUN set -xe && \
    apk add --update zeromq zeromq-dev
