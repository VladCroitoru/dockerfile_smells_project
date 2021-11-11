FROM composer:1.6.3 AS dependencies
COPY ./composer/composer.json ./composer/composer.lock /app/
WORKDIR /app
RUN composer install

FROM php:7.2.3-apache AS app
RUN mkdir /app
COPY --from=dependencies /app/vendor /app/vendor
ENV COMPOSER_VENDOR_DIR=/app/vendor
COPY src/ /var/www/html/
