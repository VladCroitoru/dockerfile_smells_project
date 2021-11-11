ARG PHP_VERSION=8.0

FROM php:${PHP_VERSION}-fpm-alpine

RUN adduser -D api && addgroup api www-data

RUN apk add --no-cache \
    supervisor \
    nginx \
    && mkdir -p /run/nginx;

# https://github.com/mlocati/docker-php-extension-installer
COPY --from=mlocati/php-extension-installer /usr/bin/install-php-extensions /usr/bin/
RUN install-php-extensions \
    bcmath \
    intl \
    pdo_pgsql \
    pgsql \
    redis \
    opcache;

COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

RUN ln -s $PHP_INI_DIR/php.ini-production $PHP_INI_DIR/php.ini

COPY config/supervisord.conf /etc/supervisor/conf.d/supervisor.d.conf
COPY config/nginx/default.conf /etc/nginx/http.d/default.conf
COPY --chown=api:api api/index.php /var/www/api/index.php

WORKDIR /var/www/api

HEALTHCHECK --interval=5s --timeout=3s \
  CMD curl -f http://localhost || exit 1

EXPOSE 80 443 9000

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisor.d.conf"]