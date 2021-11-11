FROM php:8.0-fpm
# Dockerfile author / maintainer
MAINTAINER Felix Stellmacher <docker@istsotoll.de>

COPY src/php.ini /usr/local/etc/php/
COPY src/www.conf /etc/php-fpm.d/ 
COPY src/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN apt-get update && apt-get install -y \
  supervisor \
  sudo \
  sendmail \
  s-nail \
  mariadb-client \
  bzip2 \
  libcurl4-openssl-dev \
  libfreetype6-dev \
  libicu-dev \
  libjpeg-dev \
  libjpeg62-turbo-dev \
  libldap2-dev \
  libmcrypt-dev \
  libpng-dev \
  libpq-dev \
  libxml2-dev \
  libpcre3-dev \
  libzip-dev \
  zlib1g-dev \
  libonig-dev \
  libgmp-dev \
  graphviz \
  git \
  && rm -rf /var/lib/apt/lists/*

RUN cd /usr/bin && ln -s s-nail heirloom-mailx

# https://docs.nextcloud.com/server/9/admin_manual/installation/source_installation.html
RUN docker-php-ext-configure gd --with-freetype --with-jpeg \
  && docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu \
  && docker-php-ext-install gd exif intl mbstring ldap opcache mysqli pdo_mysql pdo_pgsql pgsql zip bcmath gmp pcntl

# set recommended PHP.ini settings
# see https://secure.php.net/manual/en/opcache.installation.php
RUN { \
    echo 'opcache.memory_consumption=128'; \
    echo 'opcache.save_comments=1'; \
    echo 'opcache.enable=1'; \
    echo 'opcache.interned_strings_buffer=8'; \
    echo 'opcache.max_accelerated_files=10000'; \
    echo 'opcache.revalidate_freq=1'; \
    echo 'opcache.fast_shutdown=1'; \
    echo 'opcache.enable_cli=1'; \
  } > /usr/local/etc/php/conf.d/opcache-recommended.ini
  
# PECL extensions
RUN set -ex \
 && pecl install APCu \
 && pecl install redis \
 && docker-php-ext-enable apcu redis
 
# Install memcached
# Using master branch as workaround, as memcache is not yet released for php7
RUN set -ex \
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y libmemcached-dev \
    && rm -rf /var/lib/apt/lists/* \
    && MEMCACHED="`mktemp -d`" \
    && curl -skL https://github.com/php-memcached-dev/php-memcached/archive/master.tar.gz | tar zxf - --strip-components 1 -C $MEMCACHED \
    && docker-php-ext-configure $MEMCACHED \
    && docker-php-ext-install $MEMCACHED \
    && rm -rf $MEMCACHED

RUN groupadd -r ttrss && useradd -r -g ttrss ttrss
CMD ["/usr/bin/supervisord"]
