#rainloop-docker dockerfile
FROM php:7.1-apache

MAINTAINER tim@arctium.io

# Download rainloop source
RUN curl -O http://www.rainloop.net/repository/webmail/rainloop-community-latest.zip

# Install unzip and extract the rainloop files to the actual webserver folder
RUN apt-get update && apt-get install -y \
       unzip \
    && unzip rainloop-community-latest.zip -d /var/www/html \
    && cd /var/www/html \
    && find . -type d -exec chmod 755 {} \; \
    && find . -type f -exec chmod 644 {} \; \
    && chown -R www-data:www-data .

VOLUME /var/www/html/data
