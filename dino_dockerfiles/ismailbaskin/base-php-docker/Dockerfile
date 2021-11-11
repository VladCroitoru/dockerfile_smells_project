FROM php:7-fpm-alpine

MAINTAINER Ismail Baskin <ismailbaskin1@gmail.com>

ENV COMPOSER_NO_INTERACTION 1
ENV COMPOSER_ALLOW_SUPERUSER 1

RUN apk add --no-cache --virtual .build-deps \
            autoconf \
            make \
            g++ \
            gcc \
            libc-dev \
            pkgconf \
    && apk add --no-cache \
            postgresql-dev \
            pcre-dev \
            curl \
            git \
    && yes 'no' | pecl install -f apcu-5.1.8 \
    && docker-php-ext-enable apcu \
    && docker-php-ext-install pdo pdo_pgsql pgsql opcache zip \
    && { \
        echo 'cgi.fix_pathinfo=0'; \
        echo 'apc.stat=0'; \
        echo 'opcache.max_accelerated_files=30000'; \
        echo 'realpath_cache_size=4096K'; \
        echo 'realpath_cache_ttl=1200'; \
        echo 'display_errors=Off'; \
        echo 'file_uploads=Off'; \
        echo 'session.use_cookies=0'; \
    } | tee /usr/local/etc/php/conf.d/config.ini \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer \
    && composer global require hirak/prestissimo \
    && apk del .build-deps
