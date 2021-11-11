FROM php:7.1-fpm

MAINTAINER Caleb Favor <caleb@drumeo.com>

# Software's Installation
RUN apt-get update

RUN apt-get install -y \
        curl \
        libz-dev \
        libjpeg-dev \
        libpng12-dev \
        libfreetype6-dev \
        libssl-dev \
        libmcrypt-dev \
        nano \
        git \
        dnsutils

RUN apt-get clean

# Enable PHP Extentions
RUN docker-php-ext-install mcrypt \
  && docker-php-ext-install pdo_mysql \
  && docker-php-ext-install pcntl \
  && docker-php-ext-configure gd \
    --enable-gd-native-ttf \
    --with-jpeg-dir=/usr/lib \
    --with-freetype-dir=/usr/include/freetype2 && \
    docker-php-ext-install gd

RUN docker-php-ext-install exif
RUN docker-php-ext-configure exif \
            --enable-exif

RUN docker-php-ext-install opcache  && \
     docker-php-ext-enable opcache

RUN docker-php-ext-install mysqli

RUN docker-php-ext-install gettext

# Add PHP Config
ADD config/laravel.ini /usr/local/etc/php/conf.d
ADD config/www.conf /usr/local/etc/php-fpm.d/www.conf

# Install Composer
RUN curl -s http://getcomposer.org/installer | php && \
    mv composer.phar /usr/local/bin/composer

RUN usermod -u 1000 www-data
RUN chown -R www-data:www-data /var/www

WORKDIR /var/www

CMD ["php-fpm"]

EXPOSE 9000
