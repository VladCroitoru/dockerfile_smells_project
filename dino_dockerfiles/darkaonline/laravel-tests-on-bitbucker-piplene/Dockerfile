FROM ubuntu:17.10

MAINTAINER Darius Matulionis <darius@matulionis.lt>

ENV DEBIAN_FRONTEND noninteractive

#Set variables
ENV APPPORT=8081

RUN apt-get update -yqq --force-yes --fix-missing

RUN apt-get install -y software-properties-common python-software-properties wget locales

RUN apt-get remove -y --purge php*

RUN locale-gen en_US.UTF-8
RUN export LANG=C.UTF-8
RUN export LC_ALL=C.UTF-8

RUN LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php -y

# Update repo and install lamp, php, php dependencies, and phpmyadmin
RUN apt-get update -yqq --fix-missing

RUN apt-get -yqq --fix-missing install \
      build-essential \
      apache2 \
      curl \
      git \
      wget \
      sqlite3 \
      libpng-dev \
      libc-client-dev \
      zip \
      unzip \
      php7.2 \
      libapache2-mod-php7.2 \
      php7.2-cli \
      php7.2-mbstring \
      php7.2-mysql \
      php7.2-curl \
      php7.2-json \
      php7.2-intl \
      php7.2-gd \
      php7.2-xml \
      php7.2-zip \
      php7.2-bz2 \
      php7.2-opcache \
      php7.2-pgsql \
      php7.2-sqlite3\
      php7.2-intl \
      php7.2-bcmath \
      php7.2-soap \
      php7.2-readline


##########  Node + Yarn install  ###############
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN curl -sL https://deb.nodesource.com/setup_9.x | bash -

RUN apt-get update -yqq && apt-get -yqq --fix-missing install nodejs yarn

##########  APACHE  ##############
RUN service apache2 restart

COPY laravel.conf /etc/apache2/sites-available/laravel.conf

#This will only work with GNU sed
RUN sed -i.bak "s/Listen 80/Listen 80\n\nListen $APPPORT\n/" /etc/apache2/ports.conf

RUN a2ensite 000-default && \
    a2ensite laravel && \
    a2enmod rewrite

RUN service apache2 restart

# Downloading and installing composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

EXPOSE 80
EXPOSE 8081

WORKDIR /var/www/html
