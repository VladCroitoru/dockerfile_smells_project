FROM php:7.3-fpm-alpine

ENV XDEBUG_VERSION 2.3.3
ENV PHP_MEMORY_LIMIT 256M
ENV PHP_MAX_EXECUTION_TIME 120
ENV PHP_POST_MAX_SIZE 100M
ENV PHP_UPLOAD_MAX_FILESIZE 100M
ENV PHP_INI_DIR /usr/local/etc/php

RUN apk add --no-cache zlib-dev libzip-dev
RUN docker-php-source extract \
    && apk --no-cache --update add \
       libxml2-dev \
       libpng \
       libpng-dev \
       libjpeg-turbo \
       libjpeg-turbo-dev \
       freetype-dev \
       freetype \
       curl \
       icu-dev \
       g++ \
       autoconf \
       make \
    && rm -rf /tmp/* \
    && rm -rf /var/cache/apk/* \
    && docker-php-ext-configure bcmath \
    && docker-php-ext-configure json \
    && docker-php-ext-configure session \
    && docker-php-ext-configure ctype \
    && docker-php-ext-configure tokenizer \
    && docker-php-ext-configure simplexml \
    && docker-php-ext-configure dom \
    && docker-php-ext-configure mbstring \
    && docker-php-ext-configure zip --with-libzip \
    && docker-php-ext-configure iconv \
    && docker-php-ext-configure xml \
    && docker-php-ext-configure opcache \
    && docker-php-ext-configure pdo \
    && docker-php-ext-configure pdo_mysql \
    && docker-php-ext-configure gd --with-gd --with-freetype-dir=/usr/include/ \
      --with-jpeg-dir=/usr/include/ \
      --with-png-dir=/usr/include/ \
    && docker-php-ext-configure intl \
    && NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \
    && docker-php-ext-install -j${NPROC} gd \
    && docker-php-source delete

RUN docker-php-ext-install bcmath \
    json \
    session \
    ctype \
    tokenizer \
    simplexml \
    dom \
    mbstring \
    zip \
    iconv \
    xml \
    opcache \
    pdo \
    pdo_mysql \
    intl
RUN apk update \
    && apk add ca-certificates wget \
    && update-ca-certificates
RUN version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \
    && curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s https://blackfire.io/api/v1/releases/probe/php/alpine/amd64/$version \
    && mkdir -p /tmp/blackfire \
    && tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp/blackfire \
    && mv /tmp/blackfire/blackfire-*.so $(php -r "echo ini_get('extension_dir');")/blackfire.so \
    && printf "extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707\n" > $PHP_INI_DIR/conf.d/blackfire.ini \
    && rm -rf /tmp/blackfire /tmp/blackfire-probe.tar.gz

RUN pecl install xdebug-2.7.0RC1
RUN docker-php-ext-enable xdebug

# Xdebug settings.
COPY ./xdebug.ini /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini

# Imagemagick.
RUN apk add --no-cache imagemagick-dev
RUN pecl install imagick
RUN docker-php-ext-enable imagick
RUN apk add --no-cache --virtual .imagick-runtime-deps imagemagick

# Install mhsendmail
RUN apk update && apk add \
     go \
     git
RUN mkdir /root/go
ENV GOPATH=/root/go
ENV PATH=$PATH:$GOPATH/bin
RUN go get github.com/mailhog/mhsendmail
RUN cp /root/go/bin/mhsendmail /usr/bin/mhsendmail
COPY ./php.ini /usr/local/etc/php/conf.d/docker-php.ini

# Fix iconv lib
RUN apk add --no-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing gnu-libiconv
ENV LD_PRELOAD /usr/lib/preloadable_libiconv.so php

# Cleanup
RUN rm -rf /tmp/* \
    && rm -rf /var/cache/apk/* \
    && rm -rf tmp/*
