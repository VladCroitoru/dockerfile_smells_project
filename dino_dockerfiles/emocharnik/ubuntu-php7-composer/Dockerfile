FROM ubuntu:xenial
MAINTAINER Alex Price <alexp@fishvision.com>
ENV DEBIAN_FRONTEND noninteractive

# Remove sh
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Install packages
RUN apt-get update
RUN apt-get -y install wget \
    curl \
    git \
    zip \
    unzip \
    libxml2-dev \
    build-essential \
    libssl-dev \
    vim \
    nano \
    openssh-client \
    libreadline-gplv2-dev \
    libncursesw5-dev \
    libsqlite3-dev \
    tk-dev \
    libgdbm-dev \
    libc6-dev \
    libbz2-dev \
    software-properties-common \
    language-pack-en-base \
    ansible \
    apt-transport-https

# Add repos
RUN add-apt-repository ppa:fkrull/deadsnakes
RUN LC_ALL=en_US.UTF-8 apt-add-repository ppa:ondrej/php
RUN apt-get update

# Install PHP
RUN apt-get -y --allow-unauthenticated install \
    php7.1 \
    php7.1-cgi \
    php7.1-cli \
    php7.1-common \
    php7.1-curl \
    php7.1-dev \
    php7.1-gd \
    php7.1-gmp \
    php7.1-json \
    php7.1-ldap \
    php7.1-mysql \
    php7.1-odbc \
    php7.1-opcache \
    php7.1-pspell \
    php7.1-readline \
    php7.1-sqlite3 \
    php7.1-tidy \
    php7.1-xmlrpc \
    php7.1-xsl \
    php7.1-fpm \
    php7.1-intl \
    php7.1-mcrypt \
    php7.1-mbstring \
    php7.1-zip

# Clean apt
RUN apt-get clean

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer creates=/usr/local/bin/composer
RUN php /usr/local/bin/composer global require "fxp/composer-asset-plugin:~1.1.1"
RUN php /usr/local/bin/composer global require "hirak/prestissimo:^0.3"

# Misc
RUN mkdir -p ~/.ssh
RUN [[ -f /.dockerenv ]] && echo -e "Host *\n\tStrictHostKeyChecking no\n\n" > ~/.ssh/config
