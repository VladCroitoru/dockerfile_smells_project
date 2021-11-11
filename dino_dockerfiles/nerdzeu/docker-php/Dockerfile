FROM php:8-fpm
MAINTAINER Paolo Galeone <nessuno@nerdz.eu>

RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng-dev \
        libcurl4-openssl-dev \
        libpq-dev

RUN docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-install -j$(nproc) \
    gd \
    curl \
    sockets \
    gettext \
    pgsql \
    pdo_pgsql
RUN pecl install apcu && \
        docker-php-ext-enable apcu

# Create a group with a well-known id to work correctly with volumes
# and add the correct user to the group.
# Change the php-fpm process group to be this shared group
RUN groupadd -g 7777 nerdz && \
        gpasswd -a www-data nerdz
RUN grep -rlZ "group = www-data" /usr/local/etc/php-fpm.d | \
        xargs -0 -l sed -i -e 's/group = www-data/group = nerdz/g'
