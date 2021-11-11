# Using official Ubuntu base image
FROM ubuntu:16.04
MAINTAINER rhawnk@gmail.com

# Install Supervisor, nginx and php
RUN apt-get update && apt-get install -y supervisor \
  nginx \
  php7.0 \
  php7.0-fpm \
  php7.0-mysql \
  php7.0-curl \
  php7.0-json \
  php7.0-cgi

# Create Nginx log directory
RUN mkdir -p /var/log/nginx

# Copy our nginx config
RUN rm -Rf /etc/nginx/nginx.conf
ADD conf/nginx.conf /etc/nginx/nginx.conf

# Configure Nginx
RUN mkdir -p /etc/nginx/sites-available/ && \
mkdir -p /etc/nginx/sites-enabled/ && \
rm -Rf /var/www/* && \
mkdir -p /var/www/html/ &&\
touch /var/www/html/index.html && \
echo hello world > /var/www/html/index.html && \
echo "<?php phpinfo(); ?>" > /var/www/html/phpinfo.php

RUN rm /etc/nginx/sites-available/default
ADD conf/nginx-site.conf /etc/nginx/sites-available/default.conf
RUN ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-enabled/default.conf

# Copy Supervisor Conf.  Supervisor will manager nginx and fpm
ADD conf/supervisord.conf /etc/supervisord.conf

# Make port 80 available for links and/or publish
EXPOSE 80

# Add supervisor startup script and set to executable
ADD start_super.sh /usr/local/bin/start_super.sh
RUN chmod +x /usr/local/bin/start_super.sh

# replace the fpm socket with tcp connection
RUN sed -i 's|listen = /run/php/php7.0-fpm.sock|listen = 127.0.0.1:9000|' /etc/php/7.0/fpm/pool.d/www.conf
# enable env variable reference to fpm
RUN sed -i 's|;clear_env = no|clear_env = no|' /etc/php/7.0/fpm/pool.d/www.conf

# Define our command to be run when launching the container
CMD ["/usr/local/bin/start_super.sh"]
