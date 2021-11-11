FROM php:8.0.8-apache
MAINTAINER Shane Mc Cormack <dataforce@dataforce.org.uk>

WORKDIR /var/www

COPY errors.ini /usr/local/etc/php/conf.d/errors.ini

RUN \
  a2enmod rewrite && \
  apt-get update && apt-get install -y git unzip libz-dev libmemcached-dev libicu-dev && \
  ln -s /usr/local/bin/php /usr/bin/php && \
  docker-php-source extract && \
  docker-php-ext-install bcmath && \
  docker-php-ext-install pdo_mysql && \
  docker-php-ext-install mysqli && \
  docker-php-ext-install intl && \
  pecl install -o -f memcached && \
  docker-php-ext-enable memcached && \
  pecl install -o -f redis && \
  rm -rf /tmp/pear && \
  docker-php-ext-enable redis && \
  docker-php-source delete && \
  curl -sS https://getcomposer.org/installer | php -- --no-ansi --install-dir=/usr/bin --filename=composer

EXPOSE 80
