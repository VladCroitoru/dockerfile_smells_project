FROM ubuntu:latest

RUN sudo apt-get update && sudo apt-get install -y \
    nginx \
    php5-fpm \
    php5-cli \
    php5-mcrypt \
    git \
    mysql-server
    
RUN sudo mysql_install_db
    
# TODO: sudo nano /etc/php5/fpm/php.ini edit cgi.fix_pathinfo=0

RUN sudo php5enmod mcrypt
RUN sudo service php5-fpm restart

RUN sudo mkdir -p /var/www/laravel

# TODO: sudo nano /etc/nginx/sites-available/default

RUN curl -sS https://getcomposer.org/installer | php
RUN sudo mv composer.phar /usr/local/bin/composer

# optional
# RUN sudo composer create-project laravel/laravel /var/www/laravel

RUN sudo chown -R :www-data /var/www/laravel

# Add to working dir
WORKDIR /data/www
ADD . /data/www

RUN sudo chmod -R 775 /var/www/laravel/app/storage

RUN composer install
RUN php artisan migrate

# TODO: mysql > create database randomizr