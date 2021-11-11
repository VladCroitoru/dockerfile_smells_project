FROM alpine:3.6

ENV PERSISTANT_DEPS \
        ca-certificates \
        wget

ENV PHPIZE_DEPS \
        autoconf \
        dpkg-dev dpkg \
        file \
        g++ \
        gcc \
        libc-dev \
        make \
        pcre-dev \
        pkgconf \
        re2c \
        php7-dev

RUN apk add --no-cache --virtual .persistant-deps $PERSISTANT_DEPS \
    && apk add --no-cache --virtual .build-deps $PHPIZE_DEPS \
    && apk add --no-cache \
        git \
        openssl-dev \
        php7 \
        php7-mbstring \
        php7-dom \
        php7-phar \
        php7-pear \
        php7-openssl \
        php7-json \
        php7-tokenizer \
        php7-ctype \
        php7-session \
        php7-zlib \
    && pecl install mongodb \
    && echo "extension=mongodb.so" > /etc/php7/conf.d/mongodb.ini \
    && apk del .build-deps

RUN git clone https://github.com/tsari/xhgui.git \
    && cd xhgui \
    && php install.php

COPY config.php /xhgui/config/config.php

EXPOSE 80
CMD ["php", "-S", "0.0.0.0:80", "-t", "/xhgui/webroot"]
