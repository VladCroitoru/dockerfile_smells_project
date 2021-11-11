FROM php:7.1-fpm

MAINTAINER Niels Vermaut <niels@codingculture.com>

ENV DEBIAN_FRONTEND noninteractive

# install php
RUN apt-get update
RUN apt upgrade -y
RUN apt install -y apt-utils

RUN docker-php-ext-install -j$(nproc) pdo_mysql
RUN docker-php-ext-install -j$(nproc) mysqli
RUN docker-php-ext-install -j$(nproc) exif
RUN docker-php-ext-install -j$(nproc) gettext
RUN docker-php-ext-install -j$(nproc) pcntl
RUN docker-php-ext-install -j$(nproc) sockets
RUN docker-php-ext-install -j$(nproc) opcache

RUN sed -i "s@^access.log.*@access.log = /dev/null@" /usr/local/etc/php-fpm.d/docker.conf

RUN echo "memory_limit =-1\n" \
         "upload_max_filesize = 1000M\n" \
         "post_max_size = 1000M\n" \
         "short_open_tag = Off\n" \
         "expose_php = Off\n" \
         "display_errors = Off\n" \
         "log_errors = On\n" \
         > /usr/local/etc/php/conf.d/symfony.ini

# install nginx
RUN apt-get install -y nginx
ADD docker/nginx/vhost.conf /etc/nginx/sites-available/default

# install supervisord
RUN apt-get install -y supervisor
ADD supervisor.conf /etc/supervisord.conf
RUN mkdir /var/log/supervisord && touch /var/log/supervisord/supervisord.log
RUN touch /var/run/supervisord.pid

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]

EXPOSE 443 80

COPY . /var/www

WORKDIR /var/www