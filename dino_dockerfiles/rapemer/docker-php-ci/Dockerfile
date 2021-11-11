FROM php:8.0-cli

ARG DEBIAN_FRONTEND=noninteractive

RUN pecl channel-update pecl.php.net
RUN apt-get update
RUN apt-get install git build-essential apt-utils ssh openssh-client -y --no-install-recommends

# APCU:
RUN pecl install apcu
RUN docker-php-ext-enable apcu

# BCMATH:
RUN docker-php-ext-install bcmath

# CALENDAR:
RUN docker-php-ext-install calendar

# EXIF:
RUN docker-php-ext-install exif

# GETTEXT:
RUN docker-php-ext-install gettext

# GD:
RUN apt-get install libgd-dev libfreetype6-dev -y --no-install-recommends
RUN docker-php-ext-configure gd --with-freetype --with-jpeg
RUN docker-php-ext-install gd

# INTL:
RUN apt-get install libicu-dev -y --no-install-recommends
RUN docker-php-ext-configure intl
RUN docker-php-ext-install intl

# OPCACHE:
RUN docker-php-ext-install opcache

# PCNTL:
RUN docker-php-ext-install pcntl

# PDO:
RUN docker-php-ext-install pdo_mysql mysqli

# PostgreSQL
RUN apt-get install libpq-dev -y --no-install-recommends
RUN docker-php-ext-install pdo_pgsql pgsql

# REDIS
RUN pecl install -o -f redis
RUN rm -rf /tmp/pear
RUN docker-php-ext-enable redis

# SOAP:
RUN apt-get install libxml2-dev -y --no-install-recommends
RUN docker-php-ext-install soap

# SOCKETS:
RUN docker-php-ext-install sockets

# XSL:
RUN apt-get install libxslt-dev -y --no-install-recommends
RUN docker-php-ext-install xsl

# ZIP:
RUN apt-get install libzip-dev unzip -y --no-install-recommends
RUN docker-php-ext-install zip

# COMPOSER:
ENV COMPOSER_ALLOW_SUPERUSER=1
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# PHP settings for CI/CD
RUN echo "memory_limit = -1;" > $PHP_INI_DIR/conf.d/memory_limit.ini
RUN echo "max_execution_time = 0;" > $PHP_INI_DIR/conf.d/max_execution_time.ini
RUN echo "date.timezone = UTC;" > $PHP_INI_DIR/conf.d/timezone.ini

# DEPLOYER.org
RUN curl -o /usr/local/bin/deployer -LO https://deployer.org/deployer.phar && chmod a+x /usr/local/bin/deployer
