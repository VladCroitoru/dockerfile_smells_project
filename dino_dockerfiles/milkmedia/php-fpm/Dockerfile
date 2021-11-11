FROM php:7-fpm
RUN apt-get update && apt-get install -y postgresql libpq-dev
RUN docker-php-ext-install mbstring pdo_mysql pdo_pgsql
