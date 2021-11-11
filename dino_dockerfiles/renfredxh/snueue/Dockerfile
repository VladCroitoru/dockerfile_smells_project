# Set the base image to Ubuntu
FROM ubuntu:14.04

# File Author / Maintainer
MAINTAINER Renfred Harper

# Update the sources list
RUN apt-get update

# Install basic applications
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential software-properties-common

# Install Python and Basic Python Tools
RUN apt-get install -y python3 python3-pip

# Ruby and Compass
RUN apt-get install -y -qq ruby1.9.1-dev make
RUN gem install --no-rdoc --no-ri compass

# Node for installing Browserify and Babel
RUN apt-add-repository ppa:chris-lea/node.js
RUN apt-get update && apt-get install -y nodejs
RUN npm install -g browserify && npm install --save-dev babelify resolvify

RUN git clone https://github.com/renfredxh/snueue.git snueue
# Install the latest version of pip
RUN easy_install3 -U pip
# Get pip to download and install requirements:
RUN pip install -r /snueue/requirements.txt

EXPOSE 80

WORKDIR /snueue

# Use Gunicorn to serve the application
CMD gunicorn app:app -b 0.0.0.0:80 --log-file - --error-logfile - --access-logfile -
