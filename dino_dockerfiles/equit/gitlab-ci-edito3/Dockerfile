FROM php:7.0-fpm
MAINTAINER Kamil Kijowski <kl.kijowski@gmail.com>

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    libpq-dev \
    libzip-dev \
    libcurl4-openssl-dev \
    libfreetype6-dev \
    libicu-dev \
    libjpeg62-turbo-dev \
    libmcrypt-dev \
    libpng12-dev \
    libxslt1-dev \
    libxml2-dev \
    zlib1g-dev \
    openssh-client \
    postgresql-client \
    git-core && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN docker-php-ext-configure \
  gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/

RUN docker-php-ext-install \
  gd \
  intl \
  mcrypt \
  pdo \
  pdo_pgsql \
  pgsql \
  soap \
  xsl \
  zip \
  opcache

VOLUME /root/composer

ENV COMPOSER_HOME /root/composer

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
  composer selfupdate

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean
RUN npm install --global gulp-cli

COPY conf/php.ini /usr/local/etc/php/

WORKDIR /home/www

RUN php --version
RUN composer --version