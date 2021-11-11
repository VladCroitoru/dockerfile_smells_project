FROM ubuntu:14.04

MAINTAINER Johannes Steu hello@johannessteu.de

RUN apt-get update

RUN sudo apt-get install -y software-properties-common python-software-properties
RUN sudo LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php

RUN apt-get update
RUN apt-get install -y wget openssl php7.0 git ssh curl unzip sudo build-essential libssl-dev

RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -
RUN sudo apt-get install -y nodejs
RUN curl -sSL https://get.docker.com/ | sh


RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
RUN php -r "if (hash_file('SHA384', 'composer-setup.php') === '669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
RUN php composer-setup.php
RUN php -r "unlink('composer-setup.php');"

RUN mv composer.phar /usr/bin/composer
RUN composer self-update

RUN npm install --global gulp-cli


RUN curl -L "https://github.com/docker/compose/releases/download/1.8.1/docker-compose-$(uname -s)-$(uname -m)" > /usr/local/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose

RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl && chmod +x ./kubectl && mv ./kubectl /usr/local/bin/kubectl
