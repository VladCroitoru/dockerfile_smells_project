FROM phusion/baseimage:latest

MAINTAINER Toshie Uya <toshie.uya@gmail.com>

CMD ["/sbin/my_init"]

RUN DEBIAN_FRONTEND=noninteractive
RUN locale-gen en_US.UTF-8

ENV LANGUAGE=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
ENV LC_CTYPE=UTF-8
ENV LANG=en_US.UTF-8

RUN useradd --create-home --shell /bin/bash dev

# Add the "PHP 7" ppa
RUN apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:ondrej/php

# Install "PHP Extentions", "libraries", "Software's"
RUN apt-get update && \
    apt-get install -y --assume-yes \
        php7.1-cli \
        php7.1-common \
        php7.1-curl \
        php7.1-json \
        php7.1-xml \
        php7.1-mbstring \
        php7.1-mcrypt \
        php7.1-zip \
        php7.1-bcmath \
        pkg-config \
        php-dev \
        libcurl4-openssl-dev \
        libedit-dev \
        libssl-dev \
        libxml2-dev \
        xz-utils \
        git \
        curl \
        nano

#####################################
# Composer:
#####################################

# Install composer and add its bin to the PATH.
RUN curl -s http://getcomposer.org/installer | php && \
    mv composer.phar /usr/local/bin/composer

# Install composer plugin for concurrency
RUN composer global require hirak/prestissimo

#####################################
# PHPCS and PHPMD:
#####################################
RUN composer global require \
    squizlabs/php_codesniffer \
    phpmd/phpmd \
    phpspec/phpspec

ENV PATH=$PATH:/root/.composer/vendor/bin

#####################################
# NodeJS and npm:
#####################################
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - && \
    apt-get install -yq nodejs build-essential

# Cleaning Up

RUN apt-get clean
RUN rm -r /var/lib/apt/lists/*

ARG WORKSPACE=/

WORKDIR ${WORKSPACE}
