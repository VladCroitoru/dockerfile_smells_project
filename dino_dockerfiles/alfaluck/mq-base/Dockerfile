FROM php:7-zts

MAINTAINER Anton Shedlovsky <alfaluck@gmail.com>

RUN docker-php-ext-install -j$(nproc) mysqli \

    && pecl install redis \
    && docker-php-ext-enable redis \
# Commented now it's not needed but for PHP 7.1 PECL instalation not ready yet (12.09.2016)
#    && pecl install pthreads \
#    && docker-php-ext-enable pthreads \

    && docker-php-ext-install -j$(nproc) pcntl \

    && apt-get update \
    && apt-get install -y --no-install-recommends cron \

    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
