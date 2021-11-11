# Silex Dockerfile
#
# Version 0.0.1
FROM php:5.6-fpm-alpine
MAINTAINER Wojtek Zalewski <wojtek@neverbland.com>

LABEL   Description="This image is used to run Silex based apps" \
        Vendor="Wtk" \
        Version="0.0.1"

# Port we are going to expose
EXPOSE 8080

# Lets updates packages lists
RUN apk update --update-cache

# Lets install our system dependencies
RUN apk add \
    curl \
    git \
    openssh \
    autoconf \
    build-base

# Lets copy our php config
COPY docker/php/php.ini /usr/local/etc/php/

# Lets install few php modules
RUN pecl install \
    xdebug

# Cleaning up
RUN rm -rf \
    /var/cache/apk/* \
    /tmp/src

# @todo: Revisit this
# Now would be good time to add user which will run web-related stuff
# instead of root, especially composer install ie.
#
# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Setting up default working directory
WORKDIR /usr/src/silex

# Lets add composer file in order to install deps
ADD app/composer.json /usr/src/silex

# Install dependencies
RUN composer install --prefer-dist --working-dir=/usr/src/silex

# Enabling Xdebug
# It's done bit later because of composer.
# It has a major impact on runtime performance.
# See https://getcomposer.org/xdebug
RUN docker-php-ext-enable xdebug.so

# Lets mount volumes
VOLUME /usr/src/silex/app


