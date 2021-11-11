FROM php:5.6-apache
COPY . /var/www/html/
RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng12-dev \
     && docker-php-ext-install gd