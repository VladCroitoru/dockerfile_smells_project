FROM shubnikofff/php-apache

MAINTAINER Shubnikov Alexey <shubnikov.av@gmail.com>

COPY . /var/www/html/

RUN mv php.ini /usr/local/etc/php/conf.d/ \
    && cp -r sites-enabled/ /etc/apache2/ && rm -rf sites-enabled/ \
    && composer install --no-dev \
    && php init --env=Production --overwrite=All