# Pull from the official PHP repository
FROM php:5.6-apache

MAINTAINER Preben Uhrskov Berg <preben@uhrskov.biz>

# Update cache and get packages
RUN apt-get update && apt-get -y install \
	curl \
	zip \
	unzip \
	git

# Clone Cloud Connect demo
RUN git clone https://github.com/poulpreben/veeam-cloudconnect.git /var/www/html

# Create /veeam
RUN mkdir -p /veeam

# Copying configuration script
COPY docker-configure-restful-api.sh /veeam/docker-configure-restful-api.sh
RUN chmod +x /veeam/docker-configure-restful-api.sh

# Install Composer
RUN curl -sS https://getcomposer.org/installer | /usr/local/bin/php && /bin/mv -f composer.phar /usr/local/bin/composer

# Configure RESTful demo
RUN cd /var/www/html && composer install

# Execute this command every time the container is started
# Wrapping apache2-foreground in this file, so we can use --always-restart parameter
CMD ["/veeam/docker-configure-restful-api.sh"]