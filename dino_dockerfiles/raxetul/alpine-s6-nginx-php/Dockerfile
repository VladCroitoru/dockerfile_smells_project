FROM raxetul/alpine-s6-nginx

LABEL maintainer="Emrah URHAN <raxetul@gmail.com>"

RUN apk update && apk add --no-cache \
      php7 \
      php7-bcmath \
      php7-bz2 \
      php7-curl \
      php7-ctype \
      php7-dom \
      php7-fileinfo \
      php7-fpm \
      php7-gd \
      php7-gettext \
      php7-gmp \
      php7-iconv \
      php7-intl \
      php7-json \
      php7-mbstring \
      php7-mcrypt \
      php7-mysqli \
      php7-odbc \
      php7-opcache \
      php7-openssl \
      php7-pcntl \
      php7-pdo \
      php7-pdo_dblib \
      php7-pdo_mysql \
      php7-pdo_odbc \
      php7-pdo_pgsql \
      php7-pdo_sqlite \
      php7-pecl-apcu \
      php7-pecl-imagick \
      php7-posix \
      php7-session \
      php7-simplexml \
      php7-soap \
      php7-sqlite3 \
      php7-xmlreader \
      php7-xmlwriter \
      php7-xmlrpc \
      php7-zip \
      php7-zlib \
    && rm -rf /var/cache/apk/*
## Feedbacks for missing php modules are welcomed.

ADD php-fpm /s6/php-fpm

RUN chmod +x /s6/php-fpm/run /s6/php-fpm/finish \
    && chown root /s6/php-fpm/run /s6/php-fpm/finish \
    && mkdir -p /run/nginx && touch /run/nginx/nginx.pid \
    && echo "Fixing www.conf user and group settings, etc.. ----------" \
    && sed -i "s/;listen.owner = nobody/listen.owner = nginx/g" /etc/php7/php-fpm.d/www.conf \
    && sed -i "s/;listen.group = nobody/listen.group = nginx/g" /etc/php7/php-fpm.d/www.conf \
    && sed -i "s/user = nobody/user = nginx/g" /etc/php7/php-fpm.d/www.conf \
    && sed -i "s/group = nobody/group = nginx/g" /etc/php7/php-fpm.d/www.conf \
    && sed -i "s|;*daemonize\s*=\s*yes|daemonize = no|g" /etc/php7/php-fpm.conf \
    && sed -i "s/listen = 127.0.0.1:9000/listen = \/var\/run\/php-fpm.sock/g" /etc/php7/php-fpm.d/www.conf \
    && sed -i "s/;env/env/g" /etc/php7/php-fpm.d/www.conf \
    && echo "Enabling OPCache ----------" \
    && sed -i "s/;opcache.enable=1/opcache.enable=1/g" /etc/php7/php.ini \
    && sed -i "s/;opcache.enable_cli=0/opcache.enable_cli=1/g" /etc/php7/php.ini \
    && sed -i "s/;opcache.interned_strings_buffer=8/opcache.interned_strings_buffer=8/g" /etc/php7/php.ini \
    && sed -i "s/;opcache.max_accelerated_files=10000/opcache.max_accelerated_files=10000/g" /etc/php7/php.ini \
    && sed -i "s/;opcache.memory_consumption=128/opcache.memory_consumption=128/g" /etc/php7/php.ini \
    && sed -i "s/;opcache.save_comments=1/opcache.save_comments=1/g" /etc/php7/php.ini \
    && sed -i "s/;opcache.revalidate_freq=2/opcache.revalidate_freq=1/g" /etc/php7/php.ini \
    && echo "apc.enabled=1" >>  /etc/php7/conf.d/apcu.ini \
    && echo "apc.enable_cli=1" >>  /etc/php7/conf.d/apcu.ini

VOLUME /etc/php7/php.ini

## Don't setup ENTRYPOINT, it is set to s6 superviser in alpine-s6-base image, see Dockerfile of alpine-s6-base image
