# syntax=docker/dockerfile:1
#######################################
# Build (Base Image)
#######################################
FROM php:7.4-fpm-buster AS build

ARG ENV=DEV
ARG user=root
ARG group=root

WORKDIR "/application"

# fix debconf warnings upon build
ARG DEBIAN_FRONTEND=noninteractive

# libpng-dev needed by "gd" extension
# libzip-dev needed by "zip" extension
# libicu-dev for intl extension
RUN apt-get update \
 && apt-get install -y \
  wget \
  gnupg \
  g++ \
  locales \
  unzip \
  dialog \
  apt-utils \
  curl \
  git \
  bash \
  libpng-dev \
  libjpeg-dev \
  libfreetype6-dev \
  libzip-dev \
  libicu-dev \
  vim \
  dos2unix \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && docker-php-ext-configure gd --with-freetype --with-jpeg \
 && docker-php-ext-install \
  gd \
  intl \
  opcache \
  zip \
 && echo "UTC" > /etc/timezone \
 && dpkg-reconfigure -f noninteractive tzdata \
 && docker-php-source extract \
  pecl install opcache apcu \
  docker-php-ext-enable opcache apcu \
  docker-php-source delete \
  rm -rf /tmp/*

# Copy App
COPY composer.json /application
COPY composer.lock /application

# Install composer and vendor packages
COPY --from=composer:latest /usr/bin/composer /usr/local/bin/composer
ENV PATH="~/.composer/vendor/bin:./vendor/bin:${PATH}"

# allow webserver to use modify application
RUN chown -R $group:$user /application/

USER $user

#######################################
# Testing (Development Environment)
#######################################
FROM build AS test

# Testing uses bind volume mount
RUN mv "$PHP_INI_DIR/php.ini-development" "$PHP_INI_DIR/php.ini" \
 && composer install --no-interaction \
 && pecl install xdebug \
 && echo "xdebug.mode=coverage\n" >> "$PHP_INI_DIR/conf.d/docker-php-ext-xdebug.ini" \
 && docker-php-ext-enable xdebug \
 && rm -rf /tmp/*

#######################################
# Standard (Production Environment)
#######################################
FROM build AS standard

COPY . /application

RUN composer install --no-dev --no-interaction

#######################################
# Sphinx (Build documentation)
######################################
FROM debian:buster AS docs

LABEL os="debian" \
    service="doxyphp2sphinx"

# Install rstgenerator.py for build https://github.com/silverfoxy/doxyphp2sphinx
# PR pending made https://github.com/mike42/doxyphp2sphinx/pull/5
RUN apt-get update \
 && apt-get install --no-install-recommends -y \
      graphviz \
      imagemagick \
      make \
      python3 \
      python3-pip \
      doxygen \
      bash \
      bash-completion \
      wget \
 && python3 -m pip install --no-cache-dir -U pip \
 && python3 -m pip install --no-cache-dir Sphinx==3.4.3 Pillow \
 && pip install sphinxcontrib-phpdomain \
 && pip install sphinx_rtd_theme \
 && pip install doxyphp2sphinx \
 && apt-get update \
 && apt-get install --no-install-recommends -y \
    wget \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && wget --progress=dot:giga https://raw.githubusercontent.com/silverfoxy/doxyphp2sphinx/master/doxyphp2sphinx/rstgenerator.py \
    -O /usr/local/lib/python3.7/dist-packages/doxyphp2sphinx/rstgenerator.py

WORKDIR "/app/"

SHELL ["/bin/bash", "-c"]
