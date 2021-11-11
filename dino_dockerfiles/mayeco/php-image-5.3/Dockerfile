FROM debian:jessie

MAINTAINER Mario Young <maye.co@gmail.com>

# persistent / runtime deps
RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        libpcre3 \
        librecode0 \
        libmysqlclient-dev \
        libsqlite3-0 \
        libxml2 \
    && apt-get clean \
    && rm -r /var/lib/apt/lists/*

# phpize deps
RUN apt-get update && apt-get install -y --no-install-recommends \
        autoconf \
        file \
        g++ \
        gcc \
        libc-dev \
        make \
        pkg-config \
        re2c \
    && apt-get clean \
    && rm -r /var/lib/apt/lists/*

ENV PHP_INI_DIR /usr/local/etc/php
RUN mkdir -p $PHP_INI_DIR/conf.d

ENV GPG_KEYS 0B96609E270F565C13292B24C13C70B87267B52D 0A95E9A026542D53835E3F3A7DEC4E69FC9C83D7 0E604491
RUN set -xe \
    && for key in $GPG_KEYS; do \
        gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
    done

# compile openssl, otherwise --with-openssl won't work
RUN OPENSSL_VERSION="1.0.2d" \
        && cd /tmp \
        && mkdir openssl \
        && curl -sL "https://www.openssl.org/source/openssl-$OPENSSL_VERSION.tar.gz" -o openssl.tar.gz \
        && curl -sL "https://www.openssl.org/source/openssl-$OPENSSL_VERSION.tar.gz.asc" -o openssl.tar.gz.asc \
        && gpg --verify openssl.tar.gz.asc \
        && tar -xzf openssl.tar.gz -C openssl --strip-components=1 \
        && cd /tmp/openssl \
        && ./config && make \
        && make install \
        && make clean \
        && rm -rf /tmp/*

ENV PHP_VERSION 5.3.29

# php 5.3 needs older autoconf
# --enable-mysqlnd is included below because it's harder to compile after the fact the extensions are (since it's a plugin for several extensions, not an extension in itself)
RUN buildDeps=" \
        autoconf2.13 \
        libcurl4-openssl-dev \
        libpcre3-dev \
        libreadline6-dev \
        librecode-dev \
        libsqlite3-dev \
        libssl-dev \
        libxml2-dev \
        xz-utils \
    " \
    && set -x \
    && apt-get update && apt-get install -y --no-install-recommends $buildDeps && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN curl -SL "http://php.net/get/php-${PHP_VERSION}.tar.xz/from/this/mirror" -o php.tar.xz \
    && curl -SL "http://php.net/get/php-${PHP_VERSION}.tar.xz.asc/from/this/mirror" -o php.tar.xz.asc \
    && gpg --verify php.tar.xz.asc \
    && mkdir -p /usr/src/php \
    && tar -xof php.tar.xz -C /usr/src/php --strip-components=1 \
    && rm php.tar.xz* \
    && cd /usr/src/php \
    && ./configure \
        --with-config-file-path="$PHP_INI_DIR" \
        --with-config-file-scan-dir="$PHP_INI_DIR/conf.d" \
        --enable-fpm \
        --with-fpm-user=www-data \
        --with-fpm-group=www-data \
        --disable-cgi \
        --enable-mysqlnd \
        --with-mysql \
        --with-curl \
        --with-openssl=/usr/local/ssl \
        --with-readline \
        --with-recode \
        --with-zlib \
    && make -j"$(nproc)" \
    && make install \
    && { find /usr/local/bin /usr/local/sbin -type f -executable -exec strip --strip-all '{}' + || true; } \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false -o APT::AutoRemove::SuggestsImportant=false $buildDeps \
    && make clean

COPY docker-php-* /usr/local/bin/

RUN apt-get update && apt-get install -y --no-install-recommends libkrb5-dev libc-client-dev libpng12-dev libjpeg-dev libpq-dev \
    libmagickwand-dev libmagickcore-dev libxslt1-dev libbz2-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
    && docker-php-ext-configure imap --with-kerberos --with-imap-ssl

RUN docker-php-ext-install imap gd pdo_mysql mbstring mysqli pdo_mysql wddx zip bz2 \
    calendar exif ftp gettext shmop sockets xsl

RUN mkdir -p /usr/src/php/ext/opcache \
    && curl http://pecl.php.net/get/zendopcache-7.0.5.tgz -o zendopcache.tgz \
    && tar -xof zendopcache.tgz -C /usr/src/php/ext/opcache --strip-components=1 \
    && rm zendopcache.tgz* \
    && docker-php-ext-install opcache

RUN { \
        echo 'opcache.memory_consumption=256'; \
        echo 'opcache.interned_strings_buffer=8'; \
        echo 'opcache.max_accelerated_files=4000'; \
        echo 'opcache.revalidate_freq=180'; \
        echo 'opcache.fast_shutdown=1'; \
        echo 'opcache.enable_cli=1'; \
    } > /usr/local/etc/php/conf.d/opcache-recommended.ini

RUN { \
        echo 'zend_extension=/usr/local/lib/php/extensions/no-debug-non-zts-20090626/opcache.so'; \
    } > /usr/local/etc/php/conf.d/docker-php-ext-opcache.ini

RUN mkdir -p /imagick_source \
    && cd /imagick_source \
    && curl "http://www.imagemagick.org/download/releases/ImageMagick-6.9.2-6.tar.gz" -o imagemagick.tar.gz \
    && tar -xof imagemagick.tar.gz -C /imagick_source --strip-components=1 \
    && rm imagemagick.tar.gz* \
    && ./configure \
    && make \
    && make install \
    && make clean \
    && rm -Rf /imagick_source

RUN mkdir -p /usr/src/php/ext/imagick \
    && curl https://pecl.php.net/get/imagick-3.1.2.tgz -o imagick.tgz \
    && tar -xof imagick.tgz -C /usr/src/php/ext/imagick --strip-components=1 \
    && rm imagick.tgz* \
    && docker-php-ext-install imagick

RUN apt-get update && apt-get install -y --no-install-recommends libmemcached11 libmemcached-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/php/ext/memcached \
    && curl https://pecl.php.net/get/memcached-2.2.0.tgz -o memcached.tgz \
    && tar -xof memcached.tgz -C /usr/src/php/ext/memcached --strip-components=1 \
    && rm memcached.tgz* \
    && docker-php-ext-install memcached

RUN curl -SL https://github.com/drush-ops/drush/archive/6.6.0.tar.gz -o drush.tar.gz \
    && mkdir -p /usr/src/drush \
    && tar -xof drush.tar.gz -C /usr/src/drush --strip-components=1 \
    && rm drush.tar.gz* \
    && ln -s /usr/src/drush/drush /usr/bin
