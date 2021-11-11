FROM php:alpine
LABEL maintainer="Julien MERCIER <julien@jeckel-lab.fr>"

ENV MYSQL_HOST=mysql
ENV MYSQL_PORT=3306
ENV TIMEOUT=30

# This Dockerfile build a php image with composer included
#
# REMINDER: It's not recommanded to have composer installed in container for production as this is required for
# developpement only.

# Install system dependencies like autoconf and yaml tools
# NOTE: bash is required by wait-for-it script
RUN apk add --no-cache --virtual .build-deps \
    g++ make autoconf yaml-dev bash git

# Install PHP extensions for PDO MySQL and YAML parser
RUN docker-php-ext-install pdo_mysql && \
    pecl channel-update pecl.php.net && \
    pecl install yaml-2.0.0 && \
    docker-php-ext-enable yaml

# Install X-Debug
RUN pecl install xdebug \
        && docker-php-ext-enable xdebug

# Install composer
RUN wget https://raw.githubusercontent.com/composer/getcomposer.org/863c57de1807c99d984f7b56f0ea56ebd7e5045b/web/installer -O - -q | php -- --quiet &&\
    mv composer.phar /usr/local/bin/composer && \
    composer self-update

# Define composer cache directory
RUN mkdir -p /tmp/composer && chmod 777 /tmp/composer
ENV COMPOSER_CACHE_DIR=/tmp/composer

# Install Wait-for-it
RUN wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh -O /usr/local/bin/wait-for-it && \
    chmod +x /usr/local/bin/wait-for-it

# Install and configure SQL-Documentor
COPY . /sql-documentor
WORKDIR /sql-documentor
RUN composer install --no-dev

CMD /usr/local/bin/wait-for-it ${MYSQL_HOST}:${MYSQL_PORT} -s -t ${TIMEOUT} -- php generate.php
