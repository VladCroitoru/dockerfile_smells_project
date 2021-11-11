FROM php:fpm

MAINTAINER eric@pdxhub.org

RUN apt-get update && apt-get install -y \
      bzip2 \
      libcurl4-openssl-dev \
      libfreetype6-dev \
      libicu-dev \
      libjpeg-dev \
      libmcrypt-dev \
      libpng12-dev \
      libpq-dev \
      libxml2-dev \
      mysql-client \
      unzip \
 && rm -rf /var/lib/apt/lists/*

RUN docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
 && docker-php-ext-install exif gd intl mbstring mcrypt mysql opcache pdo_mysql zip json xmlrpc

# set recommended PHP.ini settings
# see https://secure.php.net/manual/en/opcache.installation.php
RUN { \
  echo 'opcache.memory_consumption=128'; \
  echo 'opcache.interned_strings_buffer=8'; \
  echo 'opcache.max_accelerated_files=4000'; \
  echo 'opcache.revalidate_freq=60'; \
  echo 'opcache.fast_shutdown=1'; \
  echo 'opcache.enable_cli=1'; \
} > /usr/local/etc/php/conf.d/opcache-recommended.ini

# PECL extensions
RUN pecl install APCu-4.0.10 \
 && docker-php-ext-enable apcu

VOLUME /var/www/html

COPY . /usr/src/known
COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["php-fpm"]
