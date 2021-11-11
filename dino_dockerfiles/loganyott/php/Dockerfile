FROM php:7

RUN apt-get update && apt-get install -y \
  git \
  ssh \
  tar \
  gzip
RUN \
  curl -sSL "https://github.com/composer/composer/releases/download/1.4.2/composer.phar" -o /usr/local/bin/composer && \
  chmod +x /usr/local/bin/composer
RUN pecl install xdebug && \
  docker-php-ext-enable xdebug
