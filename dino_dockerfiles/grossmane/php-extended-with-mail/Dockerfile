FROM php:7.1-apache

#ENV http_proxy http://proxy:8080
#ENV https_proxy http://proxy:8080

# Install sSMTP for mail support
RUN apt-get update \
	&& apt-get install -y -q --no-install-recommends \
		ssmtp \
	&& apt-get clean \
	&& rm -r /var/lib/apt/lists/*

COPY config/php.ini /usr/local/etc/php/
COPY config/php-mail.conf /usr/local/etc/php/conf.d/mail.ini

#ENV http_proxy=""
#ENV https_proxy=""
