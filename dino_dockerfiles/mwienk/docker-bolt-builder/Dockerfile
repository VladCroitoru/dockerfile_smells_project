FROM composer/composer
MAINTAINER Mark Wienk <mark@wienkit.nl>

ENTRYPOINT []

RUN apt-get update && apt-get install -y \
    git \
    && docker-php-ext-install pdo_mysql \
    && docker-php-ext-install exif \
    && useradd tester \
    && echo "memory_limit=1024M" > /usr/local/etc/php/conf.d/memory-limit.ini

USER tester
