FROM php:7.0.27-apache

RUN docker-php-source extract
RUN docker-php-ext-install mysqli
RUN docker-php-ext-enable mysqli
RUN docker-php-ext-install zip
RUN docker-php-ext-enable zip
RUN docker-php-source delete


COPY ./php.ini /usr/local/etc/php/

RUN a2enmod rewrite
