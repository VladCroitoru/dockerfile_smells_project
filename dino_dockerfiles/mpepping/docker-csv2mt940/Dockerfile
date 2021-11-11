FROM php:5.6-apache
MAINTAINER Martijn Pepping <martijn@xbsd.nl>

RUN mkdir -p /var/www/html/uploads \
    && chmod 1777 /var/www/html/uploads

COPY cfg/php.ini /usr/local/etc/php/

COPY app/ /var/www/html/
