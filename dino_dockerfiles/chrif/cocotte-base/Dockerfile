FROM chrif/docker

RUN apk update
RUN apk add --no-cache apache2-utils
RUN apk add --no-cache curl
RUN apk add --no-cache gettext
RUN apk add --no-cache git
RUN apk add --no-cache icu-dev
RUN apk add --no-cache libmcrypt
RUN apk add --no-cache libmcrypt-dev
RUN apk add --no-cache nginx
RUN apk add --no-cache openssh-client
RUN apk add --no-cache php7
RUN apk add --no-cache php7-ctype
RUN apk add --no-cache php7-dom
RUN apk add --no-cache php7-fpm
RUN apk add --no-cache php7-iconv
RUN apk add --no-cache php7-intl
RUN apk add --no-cache php7-json
RUN apk add --no-cache php7-mbstring
RUN apk add --no-cache php7-opcache
RUN apk add --no-cache php7-openssl
RUN apk add --no-cache php7-pdo
RUN apk add --no-cache php7-phar
RUN apk add --no-cache php7-posix
RUN apk add --no-cache php7-simplexml
RUN apk add --no-cache php7-tokenizer
RUN apk add --no-cache php7-xdebug
RUN apk add --no-cache php7-xml
RUN apk add --no-cache php7-xmlwriter
RUN apk add --no-cache php7-zlib
RUN apk add --no-cache rsync
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN rm -rf \
    ~/.composer/cache \
    /tmp/* \
    /var/cache/apk/*

RUN set -x ; \
  addgroup -g 82 -S www-data ; \
  adduser -u 82 -D -S -G www-data www-data && exit 0 ; exit 1

