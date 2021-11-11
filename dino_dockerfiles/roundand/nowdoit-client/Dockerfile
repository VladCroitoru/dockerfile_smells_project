############################################################
# Dockerfile to build Nginx Installed Containers
# Based on Ubuntu
############################################################

# Set the base image to Ubuntu
FROM ubuntu:latest

# File Author / Maintainer
MAINTAINER Francis Norton
# Install Nginx

# Add application repository URL to the default sources
#RUN echo "deb http://archive.ubuntu.com/ubuntu/ main universe" >> /etc/apt/sources.list

# Update the repository
RUN apt-get update

# Install necessary tools
RUN apt-get install -y nano wget dialog net-tools

# Download and Install Nginx
RUN apt-get install -y nginx

# Remove the default Nginx configuration file
RUN rm -v /etc/nginx/nginx.conf

# Copy a configuration file from the current directory
ADD etc/nginx/nginx.conf /etc/nginx/
ADD data /data
ADD client /client

# Append "daemon off;" to the beginning of the configuration
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# install nodejs and npm
RUN apt-get install -y nodejs-legacy npm git git-core

# Expose ports
EXPOSE 80
EXPOSE 8080

# Set the default command to execute
# when creating a new container
CMD service nginx start
