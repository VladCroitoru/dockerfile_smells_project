# This docker file is for building and running the blog API.
FROM node
MAINTAINER Martino Jones

# Install Git
RUN apt-get install git

# Get the latest build of master
RUN mkdir -p /var/www
RUN git clone https://github.com/martinoj2009/blogApi.git /var/www

# Install dependancies
RUN cd /var/www && npm install

# Expose the port
EXPOSE 8080

ENTRYPOINT cd /var/www/ && /usr/local/bin/node /var/www/api.js
