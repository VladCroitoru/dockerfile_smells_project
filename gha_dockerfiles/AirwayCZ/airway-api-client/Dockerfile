# Copied from rectorphp/rector, see https://github.com/rectorphp/rector
FROM php:7.1-cli
WORKDIR /app

# Install php extensions
RUN apt-get update && apt-get install -y \
        git \
        unzip \
        g++ \
        libzip-dev \
    && pecl -q install \
        zip \
    && docker-php-ext-configure \
        opcache --enable-opcache \
    && docker-php-ext-enable \
        zip \
        opcache

# Installing composer and prestissimo globally
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer
ENV COMPOSER_ALLOW_SUPERUSER=1 COMPOSER_MEMORY_LIMIT=-1
