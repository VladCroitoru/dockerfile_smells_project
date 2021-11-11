FROM php:5.6.26-cli

# enable git and ssh
RUN apt-get update -y && apt-get install openssh-client -y
RUN apt-get install -y zlib1g-dev git
RUN apt-get install -y libssh2-php

# enable zip to unpack composer packages
RUN docker-php-ext-install zip

# global composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer

# create .ssh directory to dump any keys and configs you might need for remote servers
RUN mkdir -p ~/.ssh

# copy composer files for deployer
COPY composer.json /composer.json
COPY composer.lock /composer.lock

# install deployer
RUN composer install