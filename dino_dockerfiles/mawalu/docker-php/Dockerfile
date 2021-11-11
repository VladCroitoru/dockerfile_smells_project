FROM ubuntu:18.04

MAINTAINER Martin Wagner <web@mawalabs.de>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y wget curl unzip git php-fpm

RUN mkdir /run/php
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN echo "clear_env = no" >> /etc/php/7.2/fpm/pool.d/www.conf

