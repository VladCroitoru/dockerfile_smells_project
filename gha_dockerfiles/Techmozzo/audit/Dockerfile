FROM php:7.4

MAINTAINER Johnson intoajohnson@gmail.com

RUN apt-get update && apt-get install -y \
libfreetype6-dev \
libjpeg62-turbo-dev \
libmcrypt-dev \
libpng-dev \
zlib1g-dev \
libxml2-dev \
libzip-dev \
libonig-dev \
graphviz \

&&  docker-php-ext-configure gd \
&&  docker-php-ext-install -j$(nproc) gd \
&&  docker-php-ext-install -j5 mbstring mysqli zip pdo pdo_mysql shmop sockets bcmath \
&&  docker-php-ext-configure zip \
&&  docker-php-source delete \
&& curl -sS https://getcomposer.org/installer | php -- \
--install-dir=/usr/local/bin --filename=composer

WORKDIR /app
COPY . .
RUN composer install
