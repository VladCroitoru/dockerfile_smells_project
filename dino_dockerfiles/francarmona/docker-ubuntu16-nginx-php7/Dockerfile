FROM ubuntu:16.04
MAINTAINER Francisco Carmona <fcarmona.olmedo@gmail.com>

# Environments vars
ENV TERM=xterm

RUN apt-get update
RUN apt-get -y upgrade

# Packages installation
RUN DEBIAN_FRONTEND=noninteractive apt-get -y --fix-missing install php7.0 \
      php7.0-cli \
      php-fpm \
      php7.0-gd \
      php7.0-json \
      php7.0-mbstring \
      php7.0-xml \
      php7.0-xsl \
      php7.0-zip \
      php7.0-soap \
      php-pear \
      curl \
      php7.0-curl \
      apt-transport-https \
      git \
      apt-transport-https \
      nano \
      lynx-cur

# Install supervisor
RUN DEBIAN_FRONTEND=noninteractive apt-get -y --fix-missing install supervisor
RUN mkdir -p /var/log/supervisor

# Install nginx (full)
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y nginx-full

# Composer install
RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer

# Nginx site conf
ADD config/nginx/nginx-site.conf /etc/nginx/sites-available/default
ADD config/nginx/nginx.conf /etc/nginx/nginx.conf

# PHP conf
ADD config/php/php.ini /etc/php/7.0/fpm/php.ini
ADD config/fpm/www.conf /etc/php/7.0/fpm/pool.d/www.conf

# Supervisor conf
ADD config/supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Add phpinfo script for INFO purposes
RUN echo "<?php phpinfo();" >> /var/www/html/index.php

WORKDIR /var/www/html/

# Create socker
RUN mkdir -p /run/php

# Volume
VOLUME /var/www/html

# Ports: nginx
EXPOSE 80
#443

CMD ["/usr/bin/supervisord"]