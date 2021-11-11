FROM php:apache
MAINTAINER Icer

# install dependency
RUN apt-get update && apt-get install -y \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libmcrypt-dev \
    libpng12-dev

RUN docker-php-ext-install -j$(nproc) iconv mcrypt \
    && docker-php-ext-install -j$(nproc) pdo_mysql \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd

COPY ./app /var/www/html/

# Modify permissions to allow plugin upload
RUN mkdir /var/www/html/tmp \
    && mkdir /var/www/html/cache \
    && chmod -R 777 /var/www/html/tmp \
    && chmod -R 777 /var/www/html/cache \
    && ln -s /var/www/html /app

RUN chown -R www-data:www-data /var/www/html/system
VOLUME  ["/app/uploads","/app/system_bak","/var/www/html/system/config"]
RUN chown -R www-data:www-data /var/www/html/system/config
COPY ./app/system/config/* /var/www/html/system/config/
