FROM php:7.3-fpm-alpine

LABEL maintainer="Michinobu Nishimoto (nismit) nismit.dev@gmail.com"

# COPY customized php.ini
COPY php.ini /usr/local/etc/php/php.ini

RUN set -ex \
        # Package Install
        # $PHPIZE_DEPS env from official image
        && apk add --no-cache --update --virtual .phpize-deps \
              $PHPIZE_DEPS \
        # Package Install For Building GD, SOAP, MEMCACHED
        # It will be deleted after build these extensions
        && apk add --no-cache --update --virtual .build-deps \
              # soap dependencies
              libxml2-dev \
              # memcached dependencies
              zlib-dev \
              libmemcached-dev \
              cyrus-sasl-dev \
              # GD dependencies
              freetype-dev \
              libjpeg-turbo-dev \
              libpng-dev \
              libwebp-dev \
              # Imagick dependencies
              libtool \
              imagemagick-dev \
        # Package Install
        && apk add --no-cache --update \
              mysql-client \
              libmemcached \
              freetype \
              libjpeg-turbo \
              libpng \
              libwebp \
              imagemagick \
        && docker-php-ext-configure gd \
              --with-freetype-dir=/usr/include \
              --with-png-dir=/usr/include \
              --with-jpeg-dir=/usr/include \
              --with-webp-dir=/usr/include \
        # Install gd opcache mysqli soap
        && docker-php-ext-install gd opcache mysqli soap \
        # Install memcached imageMagick
        && pecl install memcached imagick \
        && docker-php-ext-enable memcached imagick \
        # Delete dev packages
        && apk del .phpize-deps .build-deps \
        # Clean Up
        && rm -rf /tmp/*

# install composer and wp-cli
RUN set -ex \
        && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
        && curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar \
        && chmod +x wp-cli.phar \
        && mv wp-cli.phar /usr/local/bin/wp

# Copy and prepare entrypoint
COPY docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["php-fpm"]