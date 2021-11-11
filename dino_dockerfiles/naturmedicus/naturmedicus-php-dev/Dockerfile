FROM ubuntu:17.10

RUN apt-get update && apt-get install -my \
  curl \
  wget \
  php-curl \
  php-fpm \
  php-gd \
  php-xsl \
  php-mysqlnd \
  php-mcrypt \
  php-cli \
  php-intl \
  php-bz2 \
  php-zip \
  php-xdebug \
  php-mbstring \
  git \
  zip \
  php-apcu \
  php-opcache

RUN mkdir /run/php

ADD conf/www.conf /etc/php/7.1/fpm/pool.d/www.conf
ADD conf/memory.ini /etc/php/7.1/fpm/conf.d/memory.ini
ADD conf/upload_max_filesize.ini /etc/php/7.1/fpm/conf.d/upload_max_filesize.ini
ADD conf/opcache.ini /etc/php/7.1/mods-available/10-opcache.ini
ADD conf/apcu.ini /etc/php/7.1/mods-available/20-apcu.ini
ADD conf/apcu.ini /etc/php/7.1/mods-available/20-apcu_bc.ini
ADD conf/php-fpm.conf /etc/php/7.1/fpm/php-fpm.conf

RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer
RUN chmod +x /usr/local/bin/composer

EXPOSE 9000

CMD ["php-fpm7.1"]
