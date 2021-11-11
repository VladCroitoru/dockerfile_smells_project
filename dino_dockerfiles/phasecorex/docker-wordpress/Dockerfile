FROM wordpress:latest

MAINTAINER Ryan Foster <phasecorex@gmail.com>

RUN set -eux; \
    a2enmod ext_filter; \
    a2enmod headers; \
    pecl install redis; \
    docker-php-ext-enable redis
