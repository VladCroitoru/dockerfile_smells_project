FROM composer/composer:latest

RUN composer self-update
RUN composer clear-cache
RUN composer global require "fxp/composer-asset-plugin:^1.1"

RUN docker-php-ext-install pdo_mysql
