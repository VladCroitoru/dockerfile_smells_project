FROM php:7.4-fpm-alpine

WORKDIR /var/www/html

ADD https://raw.githubusercontent.com/mlocati/docker-php-extension-installer/master/install-php-extensions /usr/local/bin/

RUN chmod ugo+x /usr/local/bin/install-php-extensions && sync && \
    install-php-extensions pdo pdo_mysql gd zip exif

RUN docker-php-ext-install mysqli pdo pdo_mysql exif

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composerdoc