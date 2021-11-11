FROM php:7.1-fpm

ENV DEBIAN_FRONTEND noninteractive
ENV DRUSH_VERSION 8.1.0

# Common
RUN apt-get update \
    && apt-get install -y \
        git \
        openssl \
        supervisor \
        wget

RUN chmod -R 777 /tmp

#Install nginx
WORKDIR /tmp
RUN wget http://nginx.org/keys/nginx_signing.key
RUN apt-key add nginx_signing.key
COPY ./templates/nginx.list .
RUN cat /tmp/nginx.list >> /etc/apt/sources.list && rm /tmp/nginx.list
RUN apt-get update \
    && apt-get -y install \
        nginx 

WORKDIR /etc/nginx
RUN rm -Rf conf.d/default.conf

ADD ./templates/default.nginx.cnf conf.d/default.conf 

EXPOSE 80 443

# Locales
RUN apt-get update \
	&& apt-get install -y locales

RUN dpkg-reconfigure locales \
	&& locale-gen C.UTF-8 \
	&& /usr/sbin/update-locale LANG=C.UTF-8

RUN echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen \
	&& locale-gen

ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

# PHP
RUN apt-get install -y \
    bzip2 \
    curl \
    imagemagick \
    libbz2-dev \
    libc-client2007e-dev \
    libjpeg-dev \
    libkrb5-dev \
    libldap2-dev \
    libmagickwand-dev \
    libmcrypt-dev \
    libpng12-dev \
    libpq-dev \
    libxml2-dev \
    mysql-client \
    openssh-client \
    rsync \
    xfonts-base \
    xfonts-75dpi \
    && pecl install imagick \
    && docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
    && docker-php-ext-enable imagick \
    && docker-php-ext-install \
        bcmath \
        bz2 \
        calendar \
        dom \
        gd \
        json \
        mcrypt \
        mbstring \
        mysqli \
        opcache \
        pdo \
        pdo_mysql \
        soap \
        xml \
        zip

# Configure PHP-FPM

# RUN sed -i 's/listen = .*/listen = '127.0.0.0:9000'/' /usr/local/etc/php-fpm.d/www.conf

# Memcached
# TODO PECL not available for PHP 7 yet, we must compile it.
RUN apt-get install -y \
	  libmemcached-dev \
	  libmemcached11

WORKDIR /tmp
RUN git clone -b php7 https://github.com/php-memcached-dev/php-memcached \
    && cd php-memcached \
    && phpize \
    && ./configure \
    && make \
    && cp /tmp/php-memcached/modules/memcached.so /usr/local/lib/php/extensions/no-debug-non-zts-20160303/memcached.so \
    && docker-php-ext-enable memcached

# Install composer and put binary into $PATH
RUN curl -sS https://getcomposer.org/installer | php \
	&& mv composer.phar /usr/local/bin/ \
	&& ln -s /usr/local/bin/composer.phar /usr/local/bin/composer

# Set the Drush version.
RUN composer global require drush/drush:"$DRUSH_VERSION" --prefer-dist \
    && rm -f /usr/local/bin/drush \
    && ln -s ~/.composer/vendor/bin/drush /usr/local/bin/drush \
    && drush core-status -y \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /etc/supervisor

COPY ./templates/supervisord.conf conf.d/super.conf
ENTRYPOINT ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/conf.d/super.conf"]

COPY ./templates/index.php /var/www/web/index.php

WORKDIR /var/www/web

RUN apt-get -y clean \
    && apt-get -y autoclean \
    && apt-get -y autoremove