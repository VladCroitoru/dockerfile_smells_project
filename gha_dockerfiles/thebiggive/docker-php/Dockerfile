# Default Debian / Bullseye had perms issues as of 6/11/21.
# See https://stackoverflow.com/a/68900228/2803757 and
# https://github.com/thebiggive/docker-php/commit/5a0357c5939ffcbce1158ea33febc2f9c903e31e commit message.
FROM php:8.0-apache-buster

RUN apt-get update -qq  \
 && apt-get install -y git-core libicu-dev libzip-dev zip \
 && rm -rf /var/lib/apt/lists/* /var/cache/apk/*

RUN docker-php-ext-install bcmath intl pdo_mysql zip
RUN docker-php-ext-enable opcache

RUN pecl install redis && rm -rf /tmp/pear && docker-php-ext-enable redis

COPY apache/slim.conf /etc/apache2/sites-available/
COPY php/php.ini /usr/local/etc/php/

# Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN a2enmod rewrite \
 && a2enmod remoteip \
 && a2dissite 000-default \
 && a2ensite slim \
 && echo ServerName localhost >> /etc/apache2/apache2.conf
