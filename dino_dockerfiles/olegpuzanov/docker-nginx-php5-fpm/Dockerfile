# set the base image first
FROM ubuntu:14.04

# specify maintainer
MAINTAINER Oleg Puzanov <oleg.puzanov@gmail.com>

# run update and install nginx, php-fpm and other useful libraries
RUN apt-get update -y && \
	apt-get install -y \
	nginx \
	curl \
	nano \
	git \
	php5-fpm \
	php5-cli \
	php5-intl \
	php5-mcrypt \
	php5-apcu \
	php5-gd \
	php5-curl

# Add config files
ADD init /init

# run init script
RUN chmod +x /init/init.sh
RUN /init/init.sh
VOLUME ["/var/www"]

# expose port 80
EXPOSE 80

# run nginx and php5-fpm on startup
RUN echo "/etc/init.d/php5-fpm start" >> /etc/bash.bashrc
RUN echo "/etc/init.d/nginx start" >> /etc/bash.bashrc