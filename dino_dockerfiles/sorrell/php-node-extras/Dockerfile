FROM php:7.0.5-apache
RUN apt-get update && apt-get install -y \
  curl \
  git \
  imagemagick \
  libcurl4-gnutls-dev \
  libldb-dev \
  libldap2-dev \
  libpq-dev \
  libxml2-dev \
  libreoffice-writer \
  pdftk \
  zip

RUN  ln -s /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/libldap.so \
  && ln -s /usr/lib/x86_64-linux-gnu/liblber.so /usr/lib/liblber.so

RUN docker-php-ext-install -j$(nproc) \
  curl \
  json \
  ldap \
  pgsql \
  soap \
  sockets \
  xml

ENV NODE_VERSION 4.4.6

RUN curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz" \
  && curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
  && tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local --strip-components=1 \
  && rm "node-v$NODE_VERSION-linux-x64.tar.gz"

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

COPY php.ini /usr/local/etc/php

WORKDIR /var/www/html
ENV NODE_PATH /usr/local/lib/node_modules
