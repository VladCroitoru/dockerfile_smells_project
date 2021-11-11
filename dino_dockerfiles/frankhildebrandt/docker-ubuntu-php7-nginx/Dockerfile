FROM ubuntu:16.04

MAINTAINER Frank Hildebrandt <frank.hildebrandt@me.com>

RUN apt-get update \ 
 && apt-get install -y php php-mysql nginx-full curl \
 && apt-get remove --purge -y $BUILD_PACKAGES \
 && rm -rf /var/lib/apt/lists/* \
 && echo "cgi.fix_pathinfo=0" >> /etc/php/7.0/fpm/php.ini \
 && echo "access.log = /proc/self/fd/2" > /etc/php/7.0/fpm/php-fpm.log \
 && echo "error_log = /proc/self/fd/2" >> /etc/php/7.0/fpm/php-fpm.log

RUN curl -O https://bin.equinox.io/c/ekMN3bCZFUn/forego-stable-linux-amd64.tgz \
 && tar -xzf forego-stable-linux-amd64.tgz -C /usr/bin \
 && rm forego-stable-linux-amd64.tgz \
 && mkdir -p /run/php

COPY nginx.conf /etc/nginx/sites-available/default
COPY Procfile /

EXPOSE 80

ENTRYPOINT forego start