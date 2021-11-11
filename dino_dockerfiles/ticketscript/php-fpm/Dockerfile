FROM php:5.6-fpm

WORKDIR /var/www

RUN apt-get update && apt-get install -y \
        libmcrypt-dev \
        libpq5 \
        libmcrypt4 \
        libpq-dev \
        libicu-dev \
        libmemcached-dev \
        php5-cli \
        php5-xdebug \
        g++ \
        curl \
        git \
        zip \
        unzip

RUN docker-php-ext-install mcrypt \
      pdo_pgsql \
      pdo_mysql \
      opcache \
      intl \
      pgsql

RUN pecl install -f memcached
RUN echo "extension=memcached.so" >> /usr/local/etc/php/conf.d/memcached.ini

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN echo "\nphp_value[date.timezone] = Europe/Amsterdam\n" >> /usr/local/etc/php-fpm.conf

# xdebug configuration
ADD xdebug.ini /usr/local/etc/php/conf.d/ext-xdebug.ini
EXPOSE 9001
