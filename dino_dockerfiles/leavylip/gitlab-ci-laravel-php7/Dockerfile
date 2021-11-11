FROM php:7
MAINTAINER Wilbert van de Ridder <wilbert.ridder@gmail.com>
RUN apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libmcrypt-dev \
    libpng12-dev \
    libbz2-dev \
    libcurl4-openssl-dev \
    php-pear \
    curl \
    git \
    subversion \
    unzip \
  && rm -r /var/lib/apt/lists/*

# PHP Extensions
RUN docker-php-ext-install mcrypt zip bz2 mbstring \
curl \
json \
pdo_mysql \
tokenizer \
  && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
  && docker-php-ext-install gd
  
  # Run xdebug installation.
RUN curl -L https://xdebug.org/files/xdebug-2.4.0rc4.tgz >> /usr/src/php/ext/xdebug.tgz && \
    tar -xf /usr/src/php/ext/xdebug.tgz -C /usr/src/php/ext/ && \
    rm /usr/src/php/ext/xdebug.tgz && \
    docker-php-ext-install xdebug-2.4.0RC4 && \
    docker-php-ext-install pcntl && \
    php -m
  
# Memory Limit
RUN echo "memory_limit=-1" > $PHP_INI_DIR/conf.d/memory-limit.ini

# Time Zone
RUN echo "date.timezone=Europe/Amsterdam" > $PHP_INI_DIR/conf.d/date_timezone.ini

VOLUME /root/composer

# Environmental Variables
ENV COMPOSER_HOME /root/composer

# Display PHP version
RUN php --version

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
    
# Goto temporary directory.
WORKDIR /tmp

# Run composer and phpunit installation.
RUN composer selfupdate && \
    composer require "phpunit/phpunit:4.8.23" --prefer-source --no-interaction && \
    ln -s /tmp/vendor/bin/phpunit /usr/local/bin/phpunit

RUN composer --version
