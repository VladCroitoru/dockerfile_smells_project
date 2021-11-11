#
# Apache Server with PHP running on Ubuntu 14.04
#
# https://github.com/starkfell/apache-php
#

# Pull base image.
FROM ubuntu:14.04

# Maintainer contact information.
MAINTAINER Ryan Irujo <ryan.irujo@gmail.com>

# Install
RUN \
  apt-get update && apt-get install -y \
  apache2 \
  php5 \
  vim && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

# Set Apache environment variables.
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2

# Changing Web Root to display PHP pages by default.
RUN sed -i -e "/\<Directory \/var\/www\/>/a \\\tDirectoryIndex index.php" /etc/apache2/apache2.conf

# Adding index.php file to Web Root
ADD ["https://raw.githubusercontent.com/starkfell/apache-php/master/index.php","/var/www/html/"]

# Changing permissions on index.php file so it will display.
RUN chmod 775 /var/www/html/index.php

# Exposing Port 80.
EXPOSE 80

# Default command to start Apache Server.
CMD ["/usr/sbin/apache2ctl","-D","FOREGROUND"]
