FROM mawalu/docker-nginx-php

MAINTAINER Martin Wagner <web@mawalabs.de>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get install -y php-mysql php-mbstring php-gd php-curl php-dom php-zip php-sqlite3 php-xdebug php-intl php-bcmath php-soap 
RUN rm -rf /var/www/html && apt-get purge -y php-xdebug

COPY config/vhost.conf /etc/nginx/sites-available/default
