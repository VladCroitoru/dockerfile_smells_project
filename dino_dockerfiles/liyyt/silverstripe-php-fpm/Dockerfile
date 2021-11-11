FROM php:5.6-fpm-alpine
MAINTAINER Aaron Bolanos <aaron@liyyt.com>

# persistent / runtime deps
ENV BUILD_DEPS \
    autoconf \
    file \
    g++ \
    gcc \
    libc-dev \
    make \
    pkgconf \
    re2c

ENV PERSISTENT_DEPS \
    libmcrypt-dev \
    freetype-dev \
    libjpeg-turbo-dev \
    libltdl \
    libpng-dev \
    git

ENV PHP_EXT \
    gd \
    iconv \
    mbstring \
    mcrypt \
    opcache \
    pdo \
    pdo_mysql \
    mysqli

RUN set -xe \
    && apk upgrade --update \
	&& apk add --no-cache --virtual .build-deps $BUILD_DEPS \
    && apk add --no-cache --virtual .persistent-deps $PERSISTENT_DEPS \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install $PHP_EXT \
    && pecl install redis apcu intl \
    && docker-php-ext-enable --ini-name 10-redis.ini redis \
    && apk del .build-deps \
    && curl -fsSL "https://getcomposer.org/installer" -o /tmp/installer \
    && php /tmp/installer \
    && mv composer.phar /usr/local/bin/composer \
    && rm -rf /tmp/*

COPY config/php/php.ini /usr/local/etc/php/php.ini
COPY config/php-fpm.d/docker.conf /usr/local/etc/php-fpm.d/docker.conf
COPY config/php-fpm.d/www.conf /usr/local/etc/php-fpm.d/www.conf
COPY config/php-fpm.d/zz-docker.conf /usr/local/etc/php-fpm.d/zz-docker.conf

WORKDIR /var/www/html

EXPOSE 9000

CMD ["php-fpm"]