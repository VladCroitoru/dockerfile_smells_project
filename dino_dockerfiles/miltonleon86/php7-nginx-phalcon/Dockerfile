FROM ubuntu:16.04

#Install
RUN apt-get update && apt-get install -y \
git \
nginx \
php7.0-fpm \
php7.0-cli \
php7.0-gd \
curl \
vim \
wget \
php7.0-mysql \
php7.0-curl \
php7.0-intl \
php-pear \
php7.0-mcrypt \
php-memcache

#Packages for phalcon instalation	
RUN apt-get install -y gcc make re2c libpcre3-dev php7.0-dev build-essential  php7.0-zip

#Install composer
RUN curl -sS http://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer

#Install zephir
RUN composer global require "phalcon/zephir:dev-master"

#Install phalcon dev tool 
RUN composer require "phalcon/devtools" -d /usr/local/bin/
RUN ln -s /usr/local/bin/vendor/phalcon/devtools/phalcon.php /usr/bin/phalcon

#Install phalconphp with php7
RUN git clone https://github.com/phalcon/cphalcon.git -b 2.1.x --single-branch

#Building Phalcon
RUN cd cphalcon && ~/.composer/vendor/bin/zephir build --backend=ZendEngine3
RUN echo "extension=phalcon.so" >> /etc/php/7.0/fpm/conf.d/20-phalcon.ini
RUN echo "extension=phalcon.so" >> /etc/php/7.0/cli/conf.d/20-phalcon.ini

#Re-Builging
RUN ./cphalcon/ext/configure
RUN make
RUN make install

#phpInfo
RUN touch /var/www/info.php
RUN echo "<?php echo phpInfo(); ?>" > /var/www/info.php

#Networking
EXPOSE 80 443

#Nginx Conf
COPY default /etc/nginx/sites-available/
COPY default /etc/nginx/sites-enabled/

#Start sh
ADD start.sh /start.sh
RUN chmod +x /start.sh

#Starting it
ENTRYPOINT ["/start.sh"]

