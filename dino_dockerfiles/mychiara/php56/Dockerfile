#!/usr/bin/env docker

FROM mychiara/base:2.0.1
LABEL maintainer="Andy Ruck"

ENV PHP_VERSION=7.2

RUN add-apt-repository ppa:ondrej/php && apt-get update && \
  apt-get install --no-install-recommends -yq \
  imagemagick ca-certificates \
  php$PHP_VERSION php$PHP_VERSION-fpm php$PHP_VERSION-common \
  php-apcu \
  php-json \
  php-imagick \
  php-curl \
  php$PHP_VERSION-mysql php$PHP_VERSION-pgsql php-sqlite3 php-redis \
  php-xdebug php-dev && \
  curl https://getcomposer.org/installer | php -- && mv composer.phar /usr/local/bin/composer && chmod +x /usr/local/bin/composer && \
  mkdir -p /var/log/php && ln -sf /dev/stdout /var/log/php/error.log && ln -sf /dev/stdout /var/log/php5-fpm.log && \
  apt-get autoclean && apt-get -y autoremove && \
  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Copy local .inis to the image
# COPY files/php.ini /etc/php/fpm/php.ini
# COPY files/php-cli.ini /etc/php/cli/php.ini
COPY files/php-fpm.conf /etc/php/$PHP_VERSION/fpm/php-fpm.conf

# init system
RUN mkdir -p /etc/service/php-fpm /var/run/php-fpm
ADD files/start.sh /etc/service/php-fpm/run
RUN chmod +x /etc/service/php-fpm/run

EXPOSE 9000 8000
