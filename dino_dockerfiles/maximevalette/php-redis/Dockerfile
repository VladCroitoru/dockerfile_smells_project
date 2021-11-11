FROM php:5-fpm
MAINTAINER Maxime Valette <maxime@maximevalette.com>

COPY config/php.ini /usr/local/etc/php/

ADD https://pecl.php.net/get/redis-2.2.7.tgz /usr/src/php/ext/redis.tgz
RUN \
  tar -xf /usr/src/php/ext/redis.tgz -C /usr/src/php/ext/ && \
  rm /usr/src/php/ext/redis.tgz && \
  docker-php-ext-install redis-2.2.7