FROM ubuntu:16.10

MAINTAINER Toshiaki Inahata <darwin49@gmail.com>

#
# Set UP Ubuntu
#
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y wget
RUN apt-get install -y git
RUN apt-get install -y curl

#
# Install Python
#
RUN apt-get install -y python-pip python-dev
RUN pip install --upgrade pip
RUN pip install Pygments

#
# Install Node.js
#
RUN apt-get install -y nodejs npm
RUN npm cache clean
RUN npm install n -g
RUN n 6.10.2

#
# Install yarn
#
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get install -y apt-transport-https
RUN apt-get update
RUN apt-get install -y yarn
