FROM php:7.1-fpm-alpine

# Make debugging easier
RUN pecl install xdebug-2.5.0

RUN set -xe \
 && pkgs="freetype libpng libjpeg-turbo freetype-dev libpng-dev libjpeg-turbo-dev \
          libmcrypt-dev \
          postgresql-dev" \

 && apk add --no-cache $pkgs \
            --repository="http://nl.alpinelinux.org/alpine/edge/testing" \
            --repository="http://nl.alpinelinux.org/alpine/edge/community" \
            --allow-untrusted

RUN set -xe \
 && docker-php-ext-configure gd \
    --with-jpeg-dir=/usr/include/ \
    --with-png-dir=/usr/include/ \
    --with-freetype-dir=/usr/include/

RUN set -xe \
 && docker-php-ext-install -j$(getconf _NPROCESSORS_ONLN) gd iconv mcrypt exif pgsql pdo_pgsql mysqli

# We need composer
RUN set -xe \
 && php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
 && php -r "if (hash_file('SHA384', 'composer-setup.php') === trim(file_get_contents('https://composer.github.io/installer.sig'))) { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \
 && php composer-setup.php --install-dir=/bin --filename=composer && rm composer-setup.php

VOLUME ["/var/app"]

# docker build --rm --tag php-essentials-v2:7.1-fpm-alpine --file Dockerfile .
