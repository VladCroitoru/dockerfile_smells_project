FROM php:7.2.8-fpm-alpine

ENV BUILD_DEPS \
                zlib-dev \
                icu-dev \
                util-linux-dev \
                autoconf \
                g++ \
                gcc \
                make \
                pcre-dev

RUN apk update && apk add --no-cache --virtual .build-deps $BUILD_DEPS \
    && apk add bash icu-libs util-linux \
    && docker-php-ext-install zip mbstring intl opcache bcmath \
    && pecl install -o xdebug \
    && pecl install -o apcu \
    && pecl install -o uuid \
    && docker-php-ext-enable xdebug apcu uuid \
    && apk del .build-deps \
    && rm -rf /tmp/pear

RUN curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/bin/composer
