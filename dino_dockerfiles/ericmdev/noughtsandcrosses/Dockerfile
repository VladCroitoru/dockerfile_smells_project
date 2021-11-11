# Debian: NGINX + PHP-FPM (PHP-FANN)
#
# VERSION 0.0.1

# Pull the base image.
FROM debian:jessie

# Set the author.
MAINTAINER NoughtsAndCrosses

# Set environment variables.
ENV FILES docker/files/
ENV NGINX_VERSION 1.9.9-1~jessie

# Add NGINX repository source:
#
#	- nginx
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62
RUN echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >> /etc/apt/sources.list

# Install Wget Git Nano.
#
# 	- wget
# 	- git
# 	- nano
RUN apt-get update && \
    apt-get install -y wget git nano

# Install FANN.
RUN apt-get update && \
    apt-get install -y libfann-dev

# Install NGINX.
# 
# 	- openssl
# 	- ca-certificates
# 	- nginx
RUN apt-get update && \
    apt-get install -y openssl ca-certificates nginx=${NGINX_VERSION}

# Remove default configuration files.
RUN rm -rf /etc/nginx/nginx.conf
RUN rm -rf /etc/nginx/conf.d/*

# Add managed nginx configuration files.
ADD ${FILES}/etc/nginx/nginx.conf /etc/nginx/
ADD ${FILES}/etc/nginx/conf.d/noughtsandcrosses-app.conf /etc/nginx/conf.d/
ADD ${FILES}/etc/nginx/fastcgi_params /etc/nginx/
ADD ${FILES}/etc/nginx/conf.d/php-upstream.conf /etc/nginx/conf.d/upstream.conf

# Remove default directories.
RUN rm -rf /var/www/*
RUN rm -rf /srv/www/*

# Forward request and error logs to docker log collector.
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

# Install PHP 5.
#
# 	- php5-dev
#	- php5-common
#	- php5-pear
# 	- php5-cli
# 	- php5-fpm
# 	- php5-mcrypt
# 	- php5-mysql
# 	- php5-apcu
# 	- php5-gd
# 	- php5-imagick
# 	- php5-curl
# 	- php5-intl
RUN apt-get update && \
    apt-get install -y php5-dev php5-common php5-cli php5-fpm php5-mcrypt php5-mysql php5-apcu php5-gd php5-imagick php5-curl php5-intl

# Install Pecl FANN extension.
RUN pecl install fann

# Add managed php ini files.
ADD ${FILES}/etc/php5/fpm/conf.d/noughtsandcrosses-app.ini /etc/php5/fpm/conf.d/
ADD ${FILES}/etc/php5/fpm/conf.d/noughtsandcrosses-app.ini /etc/php5/cli/conf.d/
ADD ${FILES}/etc/php5/fpm/pool.d/noughtsandcrosses-app.pool.conf /etc/php5/fpm/pool.d/

# Install PHP Pimple as a C extension.
RUN git clone https://github.com/silexphp/Pimple && \
	cd Pimple/ext/pimple && \
	phpize && \
	./configure && \
	make && \
	make install

# Install Supervisor.
# 
# 	- supervisor
RUN apt-get update && \
	apt-get install -y supervisor

# Add managed supervisor configuration files.
ADD ${FILES}/etc/supervisor/conf.d/supervisord.conf /etc/supervisor/conf.d/supervisord.conf 

# Define mountable directories.
VOLUME ["/srv/www", "/etc/nginx", "/var/log/nginx/", "/var/cache/nginx"]

# Listen on http https ports.
EXPOSE 80 443

# Configure executable.
ENTRYPOINT ["/usr/bin/supervisord"]

# Define default command.
CMD []
