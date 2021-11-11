FROM ubuntu:16.04

LABEL maintainer="vinh Nguyen (quangvinh1225@gmail.vn)"

# Base php images
# Install base packages and remove the apt packages cache when done.
RUN apt-get update \
    && apt-get install -y \
        apt-utils \
	    nginx \
		supervisor \
		php \
		php-fpm \
		php-mysql \
		php-redis \
		php-curl \
		php-xml 
RUN rm -rf /var/lib/apt/lists/*

### nginx configuration
# make nginx run on the foreground
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
# Redirect log to stdout, stderr
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log
# copy and replace default nginx config
COPY nginx.conf /etc/nginx/sites-enabled/default

### php-fpm configuration
# Create directory to store socket file
RUN mkdir /run/php
# Replace default www pool
COPY phpfpm.conf /etc/php/7.0/fpm/pool.d/www.conf

### Supervisor configuration
# Replace default supervisor configuration
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

#expose ports and cmd
EXPOSE 80
CMD ["/usr/bin/supervisord"]
