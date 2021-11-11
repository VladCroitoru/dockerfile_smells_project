#FROM ubuntu:trusty
FROM php:5-apache

LABEL maintainer "Sebastian Tabares Amaya <sytabaresa@gmail.com>"

#RUN apt-get install apache2 libapache2-mod-php5 php5-pgsql php5-gd php5-xsl php5 postgresql vim
RUN apt-get update && apt-get install -y php5-pgsql php5-gd php5-xsl git postgresql-client


RUN cd /var/www/html/ && git clone http://publico:.publico@git.correlibre.org/publico/orfeo4.5 . && \
chown -R www-data:www-data .

WORKDIR /var/www/html/
# php.ini  personalizado
COPY config/php.ini /usr/local/etc/php//usr/local/etc/php/

# configuracion para postgres
COPY config/config.php.postgres config.php

RUN mkdir ./bodega && chown -R www-data ./bodega && ln -s . orfeo
VOLUME "./bodega"
