FROM ubuntu:16.04

#Install
RUN apt-get update && apt-get install -y \
git \
nginx \
php7.0-fpm \
php7.0-mysql \
php7.0-curl \
php-pear \
php7.0-mcrypt \
php-memcache

#Networking
EXPOSE 80 443

#Nginx Conf
COPY default /etc/nginx/sites-available/
COPY default /etc/nginx/sites-enabled/

#phpInfo
RUN touch /var/www/html/info.php
RUN echo "<?php echo phpInfo(); ?>" > /var/www/html/info.php

#Start sh
ADD start.sh /start.sh
RUN chmod +x /start.sh

#Starting it
ENTRYPOINT ["/start.sh"]

