###################################################################################
# Dockerfile to build a Polymer Dev Environment container images with Polymer-CLI
# Based on node:6-slim
#
# To build, do:
#   $ docker build -t fresnizky/polymer-cli .
#
###################################################################################

# Set the base image to node:6-slim
FROM node:6-slim

MAINTAINER Federico Resnizky <fresnizky@gmail.com>

RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    apt-get clean && \
    npm install -g gulp bower polymer-cli

EXPOSE 8080

RUN mkdir -p /home/node/app

VOLUME /home/node/app

WORKDIR /home/node/app

CMD ["polymer"]