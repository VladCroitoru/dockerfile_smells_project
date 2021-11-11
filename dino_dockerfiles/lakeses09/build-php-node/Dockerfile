#######################################
# BUILD-PHP-NODE
# by lakeses09 2018/02/23
#######################################
# ubuntu, php, composer, npm
#######################################

# ubuntu 16.04
FROM ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8
ENV NVM_DIR $HOME/.nvm

RUN apt-get update -qq --fix-missing \
&& apt-get upgrade -qq \
&& apt-get install -qq apt-utils \
&& apt-get install -qq curl git unzip openssl software-properties-common python-software-properties \ 
&& add-apt-repository ppa:ondrej/php \
&& apt-get update -qq \
&& apt-get install -qq php7.1 php7.1-cli php7.1-common php7.1-mysql php7.1-sqlite3 php7.1-fpm php7.1-xml \
    php7.1-curl php7.1-gd php7.1-bz2 php7.1-mcrypt php7.1-json php7.1-tidy php7.1-mbstring php-imagick \
    php-redis php-memcached \
&& curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin \
    --filename=composer creates=/usr/local/bin/composer \
&& curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash \
&& [ -s "$NVM_DIR/nvm.sh" ] \
&& \. "$NVM_DIR/nvm.sh" \
&& nvm install --lts \
&& nvm alias default lts/*

