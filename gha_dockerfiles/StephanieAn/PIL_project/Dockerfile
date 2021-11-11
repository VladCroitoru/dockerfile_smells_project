FROM php:8-apache

RUN apt-get update && apt-get install -y libxml2-dev libpq-dev && docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql
RUN docker-php-ext-install mysqli pdo_mysql pdo_pgsql pgsql session soap

RUN sed -ri 's/^www-data:x:33:33:/www-data:x:1000:50:/' /etc/passwd
