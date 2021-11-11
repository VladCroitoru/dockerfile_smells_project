###################################################
# NGINX/JEKYLL
# An image with all Nginx/Jekyll Pre-requisites and basic Nginx config.
###################################################

# Base Image
FROM nginx

# File Author / Maintainer
MAINTAINER Justin DiRose desk@justindirose.com

# Update the repository
RUN apt-get update

# Download and Install utilities

RUN apt-get install -y curl bc apt-transport-https git

# Download and install dev tools
RUN apt-get install -y rubygems ruby-dev gcc make
RUN apt-get install -y nodejs npm
RUN gem install jekyll --no-ri --no-rdoc
RUN gem install bundler

# Configure Nginx
RUN mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf.old
COPY nginx.conf /etc/nginx/nginx.conf
RUN mkdir /etc/nginx/sites-available && mkdir /etc/nginx/sites-enabled

