FROM robbertkl/php:latest
MAINTAINER Robbert Klarenbeek <robbertkl@renbeek.nl>

COPY composer.json composer.lock ./
RUN composer install --no-dev
COPY . .

COPY etc /etc

ENV DOCUMENT_ROOT=/var/www/public
VOLUME /var/www/invoices
