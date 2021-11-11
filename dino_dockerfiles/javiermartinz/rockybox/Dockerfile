FROM circleci/php:7.1-fpm-node-browsers
MAINTAINER Javier Martínez, javiermartinz

# set version label
ARG BUILD_DATE
ARG VERSION
LABEL build_version="PHP 7.1 + Node + Browsers + MySQL version:- ${VERSION} Build-date:- ${BUILD_DATE}"

# Install MySQL & PHP packages
RUN sudo wget https://repo.percona.com/apt/percona-release_0.1-4.$(lsb_release -sc)_all.deb \
    && sudo dpkg -i percona-release_0.1-4.$(lsb_release -sc)_all.deb \
    && sudo apt-get update && sudo apt-get install -y libzip-dev libpng-dev libgmp-dev \
    && sudo apt-get install -y percona-server-server-5.7 \
    && sudo rm -rf percona-release_0.1-4.jessie_all.deb \
    && sudo docker-php-ext-install zip \
    && sudo docker-php-ext-install gd \
    && sudo docker-php-ext-install gmp \
    && sudo docker-php-ext-install bcmath \
    && sudo docker-php-ext-install pdo_mysql \
    && curl -sS https://getcomposer.org/installer | sudo php -- --install-dir=/usr/local/bin --filename=composer
