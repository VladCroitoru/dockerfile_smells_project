# Base Docker image
# This gets me PHP5.6 + apache 2
FROM php:5.6-apache

# Who's neck do I wring if this doesn't work?
MAINTAINER Shaunak Kashyap shaunak.kashyap@rackspace.com

# Enable mod_rewrite
RUN a2enmod rewrite
RUN service apache2 stop

# Copy our application files into Apache's document root
ADD . /var/www/html/
