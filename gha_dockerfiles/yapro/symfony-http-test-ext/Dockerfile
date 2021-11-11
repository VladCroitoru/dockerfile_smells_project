FROM php:7-fpm-buster

# используем apt-get вместо apt, чтобы не получать: WARNING: apt does not have a stable CLI interface. Use with caution in scripts.
RUN apt-get update

# чтобы при установке apt-пакетов не возникало предупреждения: debconf: delaying package configuration, since apt-utils is not installed
RUN apt install -y apt-utils

# Чтобы composer install не выдавал ошибку: Failed to download XXX from dist: The zip extension and unzip command are both missing, skipping.
RUN apt-get install -y \
    zip \
    libzip-dev
RUN docker-php-ext-configure zip \
    && docker-php-ext-install zip

# Install composer
RUN curl https://getcomposer.org/download/2.0.12/composer.phar --output /usr/bin/composer && \
    chmod +x /usr/bin/composer

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
