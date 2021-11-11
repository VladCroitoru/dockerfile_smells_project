FROM php:7.1-fpm

RUN pecl install xdebug-2.5.0 \
    && docker-php-ext-enable xdebug

RUN apt-get update && apt-get install -y zlib1g-dev libicu-dev g++
RUN docker-php-ext-configure intl
RUN docker-php-ext-install -j$(nproc) intl

RUN apt-get update -y && apt-get install -y openssl zip unzip git
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN docker-php-ext-install pdo mysqli

RUN apt-get install -y wget curl htop

RUN apt-get install -y libpq-dev \
    && docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql \
    && docker-php-ext-install pdo_pgsql pgsql \
    && docker-php-ext-install pdo_mysql

RUN wget https://github.com/kelseyhightower/confd/releases/download/v0.15.0/confd-0.15.0-linux-amd64
RUN mkdir -p /opt/confd/bin
RUN mv confd-0.15.0-linux-amd64 /opt/confd/bin/confd
RUN chmod +x /opt/confd/bin/confd
RUN export PATH="$PATH:/opt/confd/bin"


