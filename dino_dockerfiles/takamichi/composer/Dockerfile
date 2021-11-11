FROM composer:latest

RUN set -xe; \
    : "Install parallel install plugin 'prestissimo' ..."; \
    composer global require hirak/prestissimo --no-interaction; \
    \
    apk add --update --no-cache -t .build-deps \
        autoconf \
        cmake \
        build-base; \
    \
    : "Install php-ast, Xdebug ..."; \
    pecl config-set php_ini "${PHP_INI_DIR}/php.ini"; \
    pecl install \
        ast \
        xdebug; \
    : "Enable php-ast ..."; \
    docker-php-ext-enable \
        ast; \
    \
    : "Cleanup ..."; \
    apk del --purge .build-deps; \
    pecl clear-cache; \
    composer global clear-cache;

COPY ./docker-entrypoint /usr/local/bin/

ENTRYPOINT ["docker-entrypoint"]
CMD ["composer"]
