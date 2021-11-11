# Pull base image
FROM ubuntu:14.04

MAINTAINER Visay Keo <keo@visay.info>

# Set the locales
RUN locale-gen en_US.UTF-8 en_GB.UTF-8 de_DE.UTF-8 es_ES.UTF-8 fr_FR.UTF-8 it_IT.UTF-8 km_KH sv_SE.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV DEBIAN_FRONTEND noninteractive

# Upgrade the base system
RUN apt-get update && apt-get upgrade -y -q --no-install-recommends && apt-get install -y --no-install-recommends software-properties-common

# Add ppa for PHP 7.1
RUN apt-get install -y language-pack-en-base && LC_ALL=en_US.UTF-8 add-apt-repository -y ppa:ondrej/php

# Install packages as per recommendation (https://docs.docker.com/articles/dockerfile_best-practices/)
# And clean up APT
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    sqlite3 \
    imagemagick \
    ghostscript \
    sendmail \
    openssl \
    php-ssh2 \
    php7.1-cli \
    php7.1-curl \
    php7.1-fpm \
    php7.1-gd \
    php7.1-imagick \
    php7.1-ldap \
    php7.1-mbstring \
    php7.1-mysql \
    php7.1-redis \
    php7.1-soap \
    php7.1-sqlite3 \
    php7.1-xdebug \
    php7.1-xml \
    php7.1-zip \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set workdir to project root
WORKDIR /var/www

# Copy config files for php
COPY config/app/php.ini      /etc/php/7.1/fpm/
COPY config/app/php-fpm.conf /etc/php/7.1/fpm/
COPY config/app/php-cli.ini  /etc/php/7.1/cli/
COPY config/app/www.conf     /etc/php/7.1/fpm/pool.d/

# Entry point script which wraps all commands for app container
COPY scripts/entrypoint/app.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

# By default start php-fpm
CMD ["php-fpm7.1"]
