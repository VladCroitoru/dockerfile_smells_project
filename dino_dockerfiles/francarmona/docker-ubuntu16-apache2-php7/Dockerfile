FROM ubuntu:16.04
MAINTAINER Francisco Carmona <fcarmona.olmedo@gmail.com>

# Environments vars
ENV TERM=xterm

RUN apt-get update
RUN apt-get -y upgrade

# Packages installation
RUN DEBIAN_FRONTEND=noninteractive apt-get -y --fix-missing install apache2 \
      php \
      php-cli \
      php-gd \
      php-json \
      php-mbstring \
      php-xml \
      php-xsl \
      php-zip \
      php-soap \
      php-pear \
      php-mcrypt \
      libapache2-mod-php \
      curl \
      php-curl \
      apt-transport-https \
      nano \
      lynx-cur

RUN a2enmod rewrite
RUN phpenmod mcrypt

# Composer install
RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer

# Update the default apache site with the config we created.
ADD config/apache/apache-virtual-hosts.conf /etc/apache2/sites-enabled/000-default.conf
ADD config/apache/apache2.conf /etc/apache2/apache2.conf
ADD config/apache/ports.conf /etc/apache2/ports.conf
ADD config/apache/envvars /etc/apache2/envvars

# Update php.ini
ADD config/php/php.conf /etc/php/7.0/apache2/php.ini

# Init
ADD init.sh /init.sh
RUN chmod 755 /*.sh

# Add phpinfo script for INFO purposes
RUN echo "<?php phpinfo();" >> /var/www/index.php

RUN service apache2 restart

RUN chown -R www-data:www-data /var/www

WORKDIR /var/www/

# Volume
VOLUME /var/www

# Ports: apache2
EXPOSE 80

CMD ["/init.sh"]