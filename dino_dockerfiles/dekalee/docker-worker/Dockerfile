FROM php:7.3-cli

MAINTAINER Nicolas Thal <nico.th4l@gmail.com>
MAINTAINER Jérémy GIGNON <jeremy@gignon.fr>

RUN apt-get update \
    && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng-dev \
        libcurl4-gnutls-dev \
        libpq-dev \
        zlib1g-dev \
        libicu-dev \
        libtidy-dev \
        libmagickwand-dev \
        libmagickcore-dev \
        libgeoip-dev \
        libzip-dev \
        git \
        cron \
        g++ \
        gnupg2

RUN docker-php-ext-configure intl && docker-php-ext-install intl

RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd

RUN docker-php-ext-install -j$(nproc) pdo_mysql pdo_pgsql opcache curl tidy zip

RUN pecl install imagick \
    && docker-php-ext-enable imagick

WORKDIR /tmp
RUN git clone https://github.com/Zakay/geoip.git \
    && cd geoip \
    && phpize \
    && ./configure \
    && make \
    && make install \
    && docker-php-ext-enable geoip

RUN pecl install redis-3.1.4 \
    && docker-php-ext-enable redis

RUN apt-get install -y build-essential libssl-dev libxrender-dev wget gdebi
WORKDIR /tmp
RUN wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz && \
    tar -xf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz && \
    cp wkhtmltox/bin/wkhtmltopdf /usr/local/bin && \
    cp wkhtmltox/bin/wkhtmltoimage /usr/local/bin

ADD conf.d/symfony.ini /usr/local/etc/php/conf.d/
ADD conf.d/memory.ini /usr/local/etc/php/conf.d/

RUN usermod -u 1000 www-data

RUN \
  wget -qO - https://deb.nodesource.com/setup_4.x | bash - && \
  apt-get -qq update -y && \
  apt-get -qq install -y nodejs && \
  apt-get -qq clean -y && rm -rf /var/lib/apt/lists/*

# Install StatsD
RUN \
  mkdir -p /opt && \
  cd /opt && \
  wget -qO statsd.tar.gz https://github.com/etsy/statsd/archive/v0.8.0.tar.gz && \
  tar -xzf statsd.tar.gz && \
  mv statsd-0.8.0 statsd && \
  rm -f statsd.tar.gz

RUN apt-get update \
    && apt-get install -y wget gnupg2 \
    && wget -O - https://packagecloud.io/gpg.key | apt-key add - \
    && wget -q -O - https://packages.blackfire.io/gpg.key | apt-key add - \
    && echo "deb http://packages.blackfire.io/debian any main" | tee /etc/apt/sources.list.d/blackfire.list \
    && apt-get update \
    && apt-get install blackfire-agent \
    && apt-get install blackfire-php

RUN wget http://packages.couchbase.com/releases/couchbase-release/couchbase-release-1.0-6-amd64.deb \
    && dpkg -i couchbase-release-1.0-6-amd64.deb \
    && apt-get update \
    && apt-get install -y libcouchbase-dev build-essential zlib1g-dev \
    && pecl install couchbase \
    && echo "extension=couchbase.so" > /usr/local/etc/php/conf.d/docker-php-ext-couchbase.ini
