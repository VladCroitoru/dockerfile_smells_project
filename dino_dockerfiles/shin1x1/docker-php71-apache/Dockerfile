FROM php:7.1-apache

MAINTAINER Masashi Shinbara <shin1x1@gmail.com>

# Install PHP extensions
RUN apt-get update && apt-get install -y \
      libicu-dev \
      libpq-dev \
    && rm -r /var/lib/apt/lists/* \
    && docker-php-ext-install \
      intl \
      pcntl \
      pdo_pgsql \
      pgsql \
      zip \
      opcache \
    && pecl install xdebug redis \
    && docker-php-ext-enable xdebug redis

# Install new relic
RUN echo 'deb http://apt.newrelic.com/debian/ newrelic non-free' | tee /etc/apt/sources.list.d/newrelic.list \
    && curl https://download.newrelic.com/548C16BF.gpg | apt-key add - \
    && apt-get update \
    && apt-get install -y newrelic-php5 \
    && NR_INSTALL_SILENT=1 && newrelic-install install \
    && rm -r /var/lib/apt/lists/*

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer

# Put apache config for PHP Application
COPY apache2-php-application.conf /etc/apache2/sites-available/php-application.conf
RUN a2dissite 000-default.conf && a2ensite php-application.conf && a2enmod rewrite

# Change uid and gid of apache to docker user uid/gid
RUN usermod -u 1000 www-data && groupmod -g 1000 www-data

WORKDIR /var/www/html
