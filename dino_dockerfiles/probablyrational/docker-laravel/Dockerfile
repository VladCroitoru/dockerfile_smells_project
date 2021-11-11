############################################################
# Dockerfile to build Catchall HTTP container images
# Based on php:7.0
############################################################

# Set the base image to php:7.0
FROM php:7.0-apache

# File Author / Maintainer
MAINTAINER Probably Rational Ltd.

#Set the work directory  
WORKDIR /var/www

# Installl a sweet ass profile
RUN curl -o ~/.bashrc https://gist.githubusercontent.com/hcaz/1f98157bd8ae8c647ffb3ab243d69fc8/raw/.bashrc

# Update the repository sources list
RUN apt update

# Install essentials
RUN apt install -y curl wget htop git nano xfonts-base xfonts-75dpi fontconfig xvfb libjpeg62 libxrender1 zlib1g-dev cron libmcrypt-dev libreadline-dev libfreetype6-dev libmcrypt-dev libpng12-dev libjpeg-dev libpng-dev pdftk
# Configure PHP
COPY php.ini-production /usr/local/etc/php/php.ini
RUN docker-php-ext-configure gd --enable-gd-native-ttf --with-freetype-dir=/usr/include/freetype2 --with-png-dir=/usr/include --with-jpeg-dir=/usr/include
RUN docker-php-ext-install zip pdo mysqli pdo_mysql gd mcrypt

# Install WKHTMLTOPDF
COPY wkhtmltox-0.13.0-alpha-7b36694_linux-jessie-amd64.deb wkhtmltox-0.13.0-alpha-7b36694_linux-jessie-amd64.deb
RUN dpkg -i wkhtmltox-0.13.0-alpha-7b36694_linux-jessie-amd64.deb && rm wkhtmltox-0.13.0-alpha-7b36694_linux-jessie-amd64.deb
RUN echo 'xvfb-run --server-args="-screen 0, 1024x768x24" /usr/local/bin/wkhtmltopdf $*' > /usr/bin/wkhtmltopdf.sh && chmod a+rx /usr/bin/wkhtmltopdf.sh && ln -s /usr/bin/wkhtmltopdf.sh /usr/local/sbin/wkhtmltopdf

# Install Composer
RUN mkdir -p ~/.composer/vendor/bin
RUN curl -o installer.php https://getcomposer.org/installer && php installer.php --install-dir ~/.composer/vendor/bin && rm installer.php

# Install laravel
RUN php ~/.composer/vendor/bin/composer.phar global require "laravel/installer"

# Clean up
RUN rm -rf /var/www/*

# Configure apache
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf
RUN a2enmod status rewrite

# Add a crontab
RUN touch crontab.tmp && echo '*/5 * * * * curl -fsS --retry 3 https://hchk.io/$healthcheck > /dev/null' > crontab.tmp && crontab crontab.tmp && rm -rf crontab.tmp

# Make composer work globally ;)
RUN mv ~/.composer/vendor/bin/composer.phar ~/.composer/vendor/bin/composer

# Expose ports
EXPOSE 80
