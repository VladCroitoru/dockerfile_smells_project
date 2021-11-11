FROM php:7.3-apache-stretch
RUN a2enmod rewrite
RUN docker-php-ext-install mysqli
RUN docker-php-ext-install pdo pdo_mysql mysqli
RUN usermod -u 431 www-data
RUN set -eux; apt-get update; apt-get install -y libzip-dev zlib1g-dev; docker-php-ext-install zip;