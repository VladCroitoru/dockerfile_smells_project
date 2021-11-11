#
# Apache Server running on Ubuntu 14.04
#
# https://github.com/starkfell/dockerfile/apache
#

# Pull base image.
FROM ubuntu:14.04

# Maintainer contact information.
MAINTAINER Ryan Irujo <ryan.irujo@gmail.com>

# Install
RUN \
  apt-get update && apt-get install -y \
  apache2 \
  vim && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

# Set Apache environment variables.
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2

# Exposing Port 80.
EXPOSE 80

# Default command to start Apache Server.
CMD ["/usr/sbin/apache2ctl","-D","FOREGROUND"]
