FROM php:7.1.3-apache

RUN apt-get update && \
    apt-get install -y libicu-dev && \
    docker-php-ext-install -j$(nproc) pdo pdo_mysql intl

COPY ./devops/docker/custom.ini /usr/local/etc/php/conf.d/666-custom.ini
COPY ./devops/apache/vhost.conf /etc/apache2/sites-avaliable/000-default.conf
COPY . /var/www/html

RUN rm -rf /var/www/html/devops && echo "ServerName social-media-api.local" >> /etc/apache2/apache2.conf && a2enmod rewrite

