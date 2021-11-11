FROM wouterds/rpi-php:7.0.19
MAINTAINER Wouter De Schuyter <wouter.de.schuyter@gmail.com>

# Enable cross build
RUN ["cross-build-start"]

# Make sure packages are up to date
RUN apt-get update

# Install opcache
RUN docker-php-ext-install -j$(nproc) opcache

# Install db extensions
RUN docker-php-ext-install -j$(nproc) mysqli pdo pdo_mysql

# Install mcrypt
RUN apt-get install -y libmcrypt-dev \
    && docker-php-ext-install -j$(nproc) mcrypt

# Install intl
RUN apt-get install -y libicu-dev \
    && docker-php-ext-install -j$(nproc) intl

# Install gd
RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng12-dev \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd

# Install gmp
RUN apt-get install -y libgmp-dev \
    && ln -s /usr/include/arm-linux-gnueabihf/gmp.h /usr/include/gmp.h \
    && docker-php-ext-install -j$(nproc) gmp

# Disable cross build
RUN ["cross-build-end"]
