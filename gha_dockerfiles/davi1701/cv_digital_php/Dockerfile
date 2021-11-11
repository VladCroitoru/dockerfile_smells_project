FROM php:7.3-rc-apache


RUN apt-get update -yqq \
    && apt-get -yqq install git \
    && apt-get -yqq install wget \ 
    && apt-get -yqq install apt-transport-https \ 
    && docker-php-ext-install pdo_mysql \
    && apt-get clean