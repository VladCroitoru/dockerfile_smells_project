#
# Nginx with Pagespeed
#
# https://github.com/Outlaw11A/docker-nginx-pagespeed
#

# Get our base image
FROM ubuntu:14.04

MAINTAINER Alex Price <me@alexprice.io>

# Set the versions of Nginx and Pagespeed we will use 
ENV NPS_VERSION 1.9.32.6
ENV NGINX_VERSION 1.8.0

# Install Nginx initially and some dependancies
RUN apt-get update && \
  	apt-get install -y nginx unzip libssl-dev build-essential wget libpcre3 libpcre3-dev

# Download and unzip Pagespeed
RUN cd && \
	wget https://github.com/pagespeed/ngx_pagespeed/archive/release-${NPS_VERSION}-beta.zip && \
  	unzip release-${NPS_VERSION}-beta.zip && \
  	cd ngx_pagespeed-release-${NPS_VERSION}-beta/ && \
  	wget https://dl.google.com/dl/page-speed/psol/${NPS_VERSION}.tar.gz && \
  	tar -xzvf ${NPS_VERSION}.tar.gz

# Download Nginx
RUN cd && \
  	wget http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz && \
  	tar -xvzf nginx-${NGINX_VERSION}.tar.gz && \
  	cd nginx-${NGINX_VERSION}/ && \
	./configure --add-module=/root/ngx_pagespeed-release-${NPS_VERSION}-beta --prefix=/usr/local/share/nginx --conf-path=/etc/nginx/nginx.conf --sbin-path=/usr/local/sbin --error-log-path=/var/log/nginx/error.log --with-http_ssl_module --with-http_stub_status_module --with-http_spdy_module --with-ipv6 && \
  	make && \
  	sudo make install

# Cleanup
RUN cd && \
 	rm -rf nginx-${NGINX_VERSION}/ nginx-${NGINX_VERSION}.tar.gz ngx_pagespeed-release-${NPS_VERSION}-beta/ release-${NPS_VERSION}-beta.zip && \
  	rm -rf /var/lib/apt/lists/* && \
  	echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \
  	chown -R www-data:www-data /var/lib/nginx	

# Define mountable directories.
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d", "/var/log/nginx", "/var/www/html"]

# Define working directory.
WORKDIR /etc/nginx

# Define default command.
CMD ["nginx"]

# Expose ports.
EXPOSE 80
EXPOSE 443
