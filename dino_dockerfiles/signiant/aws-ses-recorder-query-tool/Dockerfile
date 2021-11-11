FROM php:5.6-apache

# Installing git to install dependencies later 
RUN apt-get update && \
    apt-get install -y \
      git 

# Install Composer and make it available in the PATH
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer

COPY src/ /var/www/html/

WORKDIR /var/www/html/

RUN composer install --prefer-source --no-interaction

