# Application

FROM debian:jessie

MAINTAINER Vendor="lyberteam" Description="This is a new image for application"

LABEL version="1.0"

RUN apt-get update && apt-get install -y \
        mc \
        vim

RUN usermod -u 1000 www-data

RUN bash -c 'mkdir -pv /var/www/html'

RUN chown -R www-data:www-data /var/www/html
RUN chmod -R 777 /var/www/html

VOLUME "/var/www/html"
