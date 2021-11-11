FROM php:7-fpm-alpine

# Install xmlrpc extension
RUN docker-php-source extract \
    && apk add --no-cache --virtual .build-deps libxml2-dev \
    && docker-php-ext-install xmlrpc \
    && docker-php-source delete \
    && apk del .build-deps

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

COPY app/config.yml /usr/src/dyndns-updater/app/config.yml
COPY src /usr/src/dyndns-updater/src
RUN mkdir -p /usr/src/dyndns-updater/var/logs \
    && chmod 777 /usr/src/dyndns-updater/var/logs
COPY web/index.php /usr/src/dyndns-updater/web/index.php
COPY app.php /usr/src/dyndns-updater/app.php
COPY composer.json /usr/src/dyndns-updater/composer.json
COPY composer.lock /usr/src/dyndns-updater/composer.lock

WORKDIR /usr/src/dyndns-updater
RUN composer install --no-dev --optimize-autoloader