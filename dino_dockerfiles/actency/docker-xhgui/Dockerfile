# Pull base image.
FROM php:5.6-apache
COPY core/php.ini /usr/local/etc/php/

RUN apt-get update && apt-get install --fix-missing -y \
  ruby-dev rubygems \
  imagemagick graphviz \
  sudo git vim \
  memcached \
  libmemcached-tools \
  php5-memcached php5-xdebug php5-dev libpng12-dev libmcrypt-dev libxml2-dev

# Install PECL packages
COPY docker-php-pecl-install /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-php-pecl-install
RUN docker-php-pecl-install \
  xhprof-0.9.4 \
  mongo-1.6.12

COPY docker-php-ext-install /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-php-ext-install
RUN docker-php-ext-install gd mbstring mcrypt zip

# Installation of xhgui
RUN git clone https://github.com/perftools/xhgui.git /usr/share/xhgui
RUN chmod -R 0777 /usr/share/xhgui/cache
COPY core/xhgui/config.php /usr/share/xhgui/config/

# Installation of Composer
RUN cd /usr/src && curl -sS http://getcomposer.org/installer | php
RUN cd /usr/src && mv composer.phar /usr/bin/composer

RUN ln -s /usr/share/xhgui/webroot/* /var/www/html
RUN cp /usr/share/xhgui/webroot/.htaccess /var/www/html/.htaccess

RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/log/apache2 && \
  chown -R www-data:www-data /var/lock/apache2 /var/run/apache2 /var/log/apache2 /var/www/html

RUN cd /usr/share/xhgui/ && php install.php

RUN a2enmod rewrite && service apache2 restart

VOLUME /var/www/html

EXPOSE 80
CMD ["apache2-foreground"]
