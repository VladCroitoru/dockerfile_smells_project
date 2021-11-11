FROM php:7.2-fpm
LABEL maintainer="ing.brayan.cm@gmail.com"

USER root

ENV LOG_STREAM="/tmp/stdout"

# Set the locale
RUN apt-get clean && apt-get update && apt-get install -y locales\
&& sed -i -e 's/# es_MX.UTF-8 UTF-8/es_MX.UTF-8 UTF-8/' /etc/locale.gen\
&& locale-gen

ENV LANG es_MX.UTF-8
ENV LANGUAGE es_MX:es
ENV LC_ALL es_MX.UTF-8

RUN apt-get update && apt-get install -y git redis-tools libpng-dev libjpeg-dev libpq-dev libxml2-dev\
&& rm -rf /var/lib/apt/lists/* \
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
&& docker-php-ext-install gd mbstring pdo pdo_mysql pdo_pgsql zip soap

#MySQLi
RUN docker-php-ext-install mysqli opcache  && docker-php-ext-enable mysqli opcache

# APC
RUN pecl install apcu \
&& docker-php-ext-enable apcu

# Redis
RUN pecl install -o -f redis \
&&  rm -rf /tmp/pear \
&&  docker-php-ext-enable redis

#install latex
RUN apt-get update \
   && apt-get install -y \
   texlive \
   && apt-get clean \
   && rm -rf /var/lib/apt/lists/*

# ssh2
RUN apt-get update && \
apt-get install -y gcc make autoconf libc-dev pkg-config \
&& apt-get install -y libssh2-1-dev \
&& pecl install ssh2-1.1.2 \
&& docker-php-ext-enable ssh2

RUN mkfifo $LOG_STREAM && chmod 777 $LOG_STREAM
CMD ["/bin/sh", "-c", "php-fpm -D | tail -f $LOG_STREAM"]

EXPOSE 9000