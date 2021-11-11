FROM circleci/php:7.4-fpm-buster-node-browsers-legacy

## Upgrade all dependencies and global composer version and set defaults for php and add needed nginx sources
RUN sudo apt-get upgrade -y && sudo composer self-update \
    && sudo npm i -g npm@6 \
    && sudo mkdir -p /home/cirlceci/project && sudo chmod 770 /home/cirlceci/project \
    && echo "date.timezone = UTC" | sudo tee /usr/local/etc/php/conf.d/date.ini \
    && echo "memory_limit = -1" | sudo tee /usr/local/etc/php/conf.d/memory.ini \
    && echo "deb http://nginx.org/packages/debian/ buster nginx" | sudo tee --append /etc/apt/sources.list \
    && echo "deb-src http://nginx.org/packages/debian/ buster nginx" | sudo tee --append /etc/apt/sources.list

## Add nginx key signing for apt
RUN sudo wget https://nginx.org/keys/nginx_signing.key \
    && sudo apt-key add nginx_signing.key

## Install nginx and supervisor
RUN sudo apt-get update && sudo apt-get install -y nginx supervisor

## Install node and php extensions
RUN sudo apt-get install -y autoconf libmemcached-dev libicu-dev libxml2-dev \
                            libfreetype6-dev libjpeg62-turbo-dev exiftool \
                            libgd-dev libpng-dev libjpeg-dev zlib1g-dev \
                            default-mysql-client xvfb chromium \
    && sudo pecl install memcached \
    && sudo docker-php-ext-enable memcached \
    && sudo pecl install redis \
    && sudo docker-php-ext-enable redis \
    && sudo docker-php-ext-configure intl \
    && sudo docker-php-ext-install intl \
    && sudo docker-php-ext-configure exif \
    && sudo docker-php-ext-install exif \
    && sudo docker-php-ext-enable exif \
    && sudo docker-php-ext-install zip \
    && sudo docker-php-ext-install pcntl \
    && sudo docker-php-ext-install bcmath \
    && sudo docker-php-ext-configure gd --with-freetype=/usr/include/ --with-jpeg=/usr/include/ \
    && sudo docker-php-ext-install gd \
    && sudo docker-php-ext-install soap \
    && sudo docker-php-ext-install mysqli \
    && sudo docker-php-ext-install pdo_mysql \
    && sudo docker-php-ext-install sockets

## Remove default nginx config
RUN sudo rm /etc/nginx/conf.d/default.conf
## Add default nginx config
ADD conf/default.nginx.conf /etc/nginx/conf.d/default.conf

## Add supervisord configs for nginx/php-fpm
ADD conf/nginx.supervisord.conf /etc/supervisor/conf.d/nginx.conf
ADD conf/php-fpm.supervisord.conf /etc/supervisor/conf.d/php-fpm.conf

## Run autoremove
RUN sudo apt-get --purge autoremove

CMD sudo /usr/bin/supervisord -n -c /etc/supervisor/supervisord.conf
