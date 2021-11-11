FROM php:fpm-alpine
MAINTAINER Jacques Moati <jacques@moati.net>

RUN apk --update \
        --repository http://dl-3.alpinelinux.org/alpine/v3.6/main/ \
        upgrade && \

    apk --update \
        --repository http://dl-3.alpinelinux.org/alpine/v3.6/main/ \
        --repository http://dl-3.alpinelinux.org/alpine/v3.6/community/ \
        add bash shadow openssl icu icu-dev curl libtool imagemagick-dev make g++ autoconf perl rabbitmq-c-dev freetype-dev libjpeg-turbo-dev libmcrypt-dev libpng-dev pcre-dev libxml2-dev ttf-freefont libgcc libstdc++ libx11 glib libxrender libxext libintl libcrypto1.0 libssl1.0 ttf-dejavu ttf-droid ttf-freefont ttf-liberation ttf-ubuntu-font-family libmemcached-dev cyrus-sasl-dev && \
    apk --update \
        --repository http://dl-3.alpinelinux.org/alpine/edge/community/ \
        add jpegoptim && \
    docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ && \
    docker-php-ext-install iconv mcrypt gd bcmath exif intl opcache pcntl sockets zip pdo_mysql soap calendar mysqli && \
    pecl install imagick amqp redis memcached && \
    docker-php-ext-enable imagick amqp redis memcached && \

    apk del --purge make g++ autoconf libtool && \
    rm -rf /var/cache/apk/*

COPY run.sh /run.sh

COPY wkhtmltopdf /usr/local/bin

COPY php.ini /usr/local/etc/php/

EXPOSE 9000

CMD /run.sh
