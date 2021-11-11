################################
# Dockerfile for depressionbot #
################################

# Set base image (Alpine v3.6)
FROM node:8-alpine

# Set maintainer.
LABEL maintainer="Dom Rodriguez <shymega@shymega.org.uk>"

# Phase 0 - package installation
RUN apk add --update git wget unzip bash

# Phase 1 - create Docker user
RUN addgroup -S docker \
  && adduser -S docker -h /docker \
  && adduser docker docker

# Set user for the installation
USER docker

# Phase 2 - setup dbot.
# Clone dbot into /docker/dbot
RUN git clone https://github.com/reality/dbot.git /docker/dbot

# Install dbot using the provided script.
WORKDIR /docker/dbot
RUN EDITOR=/bin/true /docker/dbot/install

# Phase 3 - cleanup.

# Set user back to root to cleanup
USER root
RUN apk del --no-cache --rdepends git py-pip g++ make

# Set user back to docker use for runtime execution
USER docker

# Set runtime command.
CMD ["node", "/docker/dbot/run.js"]
