FROM php:5.6-fpm
MAINTAINER Sebastian Nagels <sebastian.nagels@active-value.de>

ENV APPLICATION_NAME project
ENV COMPOSER_VERSION 1.3.2

# Install dependencies
RUN apt-get update && apt-get install -y \
      ca-certificates \
      libicu-dev \
      libpng-dev \
      libjpeg-dev \
      libxml2 \
      libxml2-dev \
      libfreetype6-dev \
      libjpeg62-turbo-dev \
      libmcrypt-dev \
      libpq-dev \
      libcurl3 \
      libcurl3-dev \
      libpng12-dev \
      bzip2 \
      curl \
      wget \
      git \
      locales \
      libssl-dev \
      zlib1g-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean \

    && echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen \
    && locale-gen

# Environment Layer
RUN pecl install \
      mongodb \
      apcu-4.0.11 \
      redis \
    && docker-php-ext-enable \
      mongodb \
      apcu \
      redis \
    && rm -rf /tmp/pear \

    && docker-php-ext-install -j$(nproc) \
        zip \
        intl \
        mbstring \
        exif \
        bcmath \
        pdo \
        pdo_mysql \
        pdo_pgsql \
        curl \
        opcache \
        iconv \
        mcrypt \
        soap \
    && docker-php-ext-configure gd \
        --with-freetype-dir=/usr/include/ \
        --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd

# Added local Cache and Log Directory
RUN mkdir -p \
      /var/cache/${APPLICATION_NAME} \
      /var/log/${APPLICATION_NAME} \
    && chmod 777 \
      /var/cache/${APPLICATION_NAME} \
      /var/log/${APPLICATION_NAME}

RUN usermod -u 1000 www-data

# Install Composer Global
RUN php -r "copy('https://getcomposer.org/installer', '/tmp/composer-setup.php');" \
    && php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin --filename=composer --version=${COMPOSER_VERSION} \
    && rm -rf /tmp/composer-setup.php

# XDEBUG
RUN pecl install xdebug
RUN touch /usr/local/etc/php/conf.d/xdebug.ini; \
    echo "zend_extension = $(find /usr/local/lib/php/extensions/ -name xdebug.so)" >> /usr/local/etc/php/conf.d/xdebug.ini; \
    echo "xdebug.remote_enable=1" >> /usr/local/etc/php/conf.d/xdebug.ini; \
    echo "xdebug.idekey=PHPSTORM" >> /usr/local/etc/php/conf.d/xdebug.ini; \
    echo "xdebug.remote_autostart=0" >> /usr/local/etc/php/conf.d/xdebug.ini; \
    echo "xdebug.remote_log=/tmp/php5-xdebug.log" >> /usr/local/etc/php/conf.d/xdebug.ini;
