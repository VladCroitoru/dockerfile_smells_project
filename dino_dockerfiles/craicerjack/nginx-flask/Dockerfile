############################################################
# Dockerfile to build Flask App
# Based on
############################################################

# Set the base image
FROM debian:latest

# File Author / Maintainer
MAINTAINER Carlos Tighe

COPY ./nginx_signing.key /var/www/app/nginx_signing.key
RUN apt-key add /var/www/app/nginx_signing.key
RUN echo "deb http://nginx.org/packages/debian/ jessie nginx" >> /etc/apt/sources.list
RUN echo "deb-src http://nginx.org/packages/debian/ jessie nginx" >> /etc/apt/sources.list

RUN apt-get update && apt-get install -y nginx \
    build-essential \
    python \
    python-dev\
    python-pip \
 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/*

 # Copy over and install the requirements
COPY ./app/requirements.txt /var/www/app/app/requirements.txt
RUN pip install -r /var/www/app/app/requirements.txt

COPY ./run.py ./uwsgi.ini ./app.conf /var/www/app/
RUN rm /etc/nginx/conf.d/default.conf && ln -s /var/www/app/app.conf /etc/nginx/conf.d/
COPY ./app /var/www/app/app/

WORKDIR /var/www/app

EXPOSE 80

CMD ["/bin/bash", "-c", "nginx; uwsgi uwsgi.ini"]

