############################################################
# Dockerfile to build a Slocker container
# Based on Debian
# https://github.com/julienstroheker/Slocker
############################################################

# Set the base image
FROM julienstroheker/pythonflask

# File Author / Maintainer
MAINTAINER Julien Stroheker

# Create app folder, where the magic is !
RUN mkdir -p /usr/src/app

# Set the default directory where CMD will execute
WORKDIR /usr/src/app

# Copy the application folder inside the container
COPY app /usr/src/app

# Expose port
EXPOSE 8080