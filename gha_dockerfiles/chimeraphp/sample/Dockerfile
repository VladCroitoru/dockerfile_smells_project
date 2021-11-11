FROM php:7.4-alpine as base

ENV APPLICATION_MODE=prod
WORKDIR /opt/chimera/sample

RUN apk add --no-cache git \
    && apk add --no-cache --virtual .build $PHPIZE_DEPS \
    && docker-php-ext-install pcntl opcache \
    && rm -f "/usr/src/php.tar.xz" "/usr/src/php.tar.xz.asc" \
    && docker-php-source delete \
    && rm /usr/local/bin/phpdbg \
    && rm -rf /tmp/pear ~/.pearrc \
    && apk del .build

RUN { \
    echo 'zend.assertions=-1'; \
    echo 'assert.exception=1'; \
    echo 'opcache.enable_cli=1'; \
    echo 'opcache.max_wasted_percentage=10'; \
    echo 'opcache.validate_timestamps=0'; \
    echo 'opcache.enable_file_override=1'; \
    echo 'opcache.optimization_level=0xFFFFFFFF'; \
    echo 'error_reporting=E_ALL & ~E_DEPRECATED & ~E_USER_DEPRECATED & ~E_STRICT'; \
    echo 'display_errors=0'; \
    echo 'log_errors=1'; \
    echo 'error_log=/dev/stderr'; \
    echo 'short_open_tag=0'; \
    echo 'zend.exception_ignore_args=1'; \
} | tee /usr/local/etc/php/conf.d/10-prod.ini

FROM base as build

COPY --from=composer:2 /usr/bin/composer /usr/bin/composer
COPY composer.* ./

RUN composer install --no-dev --no-autoloader

COPY . .

RUN composer dumpautoload --no-dev -a \
    && mkdir -p var/cache var/tmp \
    && php public/index.php || true \
    && echo '[]' > var/tmp/books.json \
    && chmod 777 var/tmp/books.json

FROM base

COPY --from=build /opt/chimera/sample/ /opt/chimera/sample/

CMD ["php", "-S", "0.0.0.0:80", "-t", "public"]
