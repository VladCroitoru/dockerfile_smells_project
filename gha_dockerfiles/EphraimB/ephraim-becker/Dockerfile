FROM php:8.0-apache
COPY ./ /var/www/html/

RUN apt-get update -y && apt-get install -y libpng-dev libjpeg-dev

RUN apt-get update && \
    apt-get install -y \
        zlib1g-dev

RUN docker-php-ext-configure gd --enable-gd --with-jpeg
RUN docker-php-ext-install mysqli gd exif
