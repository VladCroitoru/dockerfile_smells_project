FROM node:8.3.0-stretch
MAINTAINER Rolf Larsen

RUN git clone https://github.com/rhodiumlabs/node-mjpeg-proxy.git \
#  && cd node-mjpeg-proxy \
  && npm install express \
  && npm install mjpeg-proxy

#
# Define an environment variable
# 
# Use this variable when creating a container to specify the MJPEG host.
ENV MJPEG_URL=""

ADD index.js /

CMD nodejs index.js
