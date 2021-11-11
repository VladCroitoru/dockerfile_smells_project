FROM php:7.0.9-fpm
MAINTAINER Hardik Gajjar <hardik.gajjar@inviqa.com>

RUN apt-get update \
  && apt-get install -y \
    cron \
    libfreetype6-dev \
    libicu-dev \
    libjpeg62-turbo-dev \
    libmcrypt-dev \
    libpng12-dev \
    libxslt1-dev \
    git

RUN docker-php-ext-configure \
  gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/

RUN docker-php-ext-install \
  gd \
  intl \
  mbstring \
  mcrypt \
  pdo_mysql \
  soap \
  xsl \
  zip \
  bcmath

RUN pecl install xdebug-2.4.0

RUN echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \
      && echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini \
      && echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/xdebug.ini

RUN curl -sS https://getcomposer.org/installer | \
    php -- \
      --install-dir=/usr/local/bin \
      --filename=composer \
      --version=1.1.2

# compile and install php7 redis extension
RUN apt-get install -y redis-tools \
  && git clone https://github.com/phpredis/phpredis.git \
  && cd phpredis && git checkout php7 && phpize && ./configure && make && make install && cd .. && rm -rf phpredis \
  && echo "extension=redis.so" > /usr/local/etc/php/conf.d/redis.ini

# compile and install php7 memcached extension
RUN curl -Ls -O https://launchpad.net/libmemcached/1.0/1.0.18/+download/libmemcached-1.0.18.tar.gz \
  && tar -xvf libmemcached-1.0.18.tar.gz  && cd libmemcached-1.0.18 && ./configure --disable-memcached-sasl && make && make install && cd .. && rm -rf libmemcached-1.0.18 \
  && git clone https://github.com/php-memcached-dev/php-memcached.git \
  && cd php-memcached && git checkout php7 && phpize && ./configure --disable-memcached-sasl && make && make install && cd .. && rm -rf php-memcached \
  && echo "extension=memcached.so" > /usr/local/etc/php/conf.d/memcached.ini

# install node, npm and grunt
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && apt-get install -y nodejs && npm install -g grunt

ENV PHP_MEMORY_LIMIT 2G
ENV PHP_PORT 9000
ENV PHP_PM dynamic
ENV PHP_PM_MAX_CHILDREN 10
ENV PHP_PM_START_SERVERS 4
ENV PHP_PM_MIN_SPARE_SERVERS 2
ENV PHP_PM_MAX_SPARE_SERVERS 6
ENV APP_MAGE_MODE default

COPY conf/www.conf /usr/local/etc/php-fpm.d/
COPY conf/php.ini /usr/local/etc/php/
COPY conf/php-fpm.conf /usr/local/etc/
COPY bin/* /usr/local/bin/

WORKDIR /var/www

CMD ["/usr/local/bin/start"]
