FROM php:7.4-fpm

MAINTAINER Yoann Frommelt <yoann@frommelt.fr>

# Set correct environment variables.
ENV DEBIAN_FRONTEND=noninteractive
ENV HOME /root

# Ubuntu mirrors
RUN apt-get update

# Install requirements for standard builds.
RUN apt-get install --no-install-recommends -y \
        apt-transport-https \
        build-essential \
        bzip2 \
        ca-certificates \
        curl \
        git \
        gnupg \
        libfreetype6-dev \
        libicu-dev \
        libjpeg-dev \
        libjpeg62-turbo-dev \
        libmemcached-dev \
        libpng-dev \
        libonig-dev \
        libpq-dev \
        libssl-dev \
        libz-dev \
        libzip-dev \
        openssh-client \
        rsync \
        unzip \
        wget

# Repo for Node
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash
RUN apt-get install -y nodejs

# Repo for Yarn
RUN npm install -g yarn

# Standard cleanup
RUN apt-get autoremove -y && \
    update-ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install common PHP packages.
RUN docker-php-ext-install \
    iconv \
    mbstring \
    bcmath \
    intl \
    pdo \
    pdo_mysql \
    pdo_pgsql \
    zip

# Install the PHP gd library
RUN docker-php-ext-configure gd --with-freetype --with-jpeg && \
    docker-php-ext-install gd

# Install Xdebug
RUN pecl install xdebug && docker-php-ext-enable xdebug \
  && echo "error_reporting = E_ALL" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
  && echo "display_startup_errors = On" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
  && echo "display_errors = On" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini

# Install composer
RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer

# Add fingerprints for common sites.
RUN mkdir ~/.ssh && \
    ssh-keyscan -H github.com >> ~/.ssh/known_hosts && \
    ssh-keyscan -H gitlab.com >> ~/.ssh/known_hosts

# Show versions
RUN php -v && \
    node -v && \
    npm -v && \
    yarn -v

CMD ["bash"]