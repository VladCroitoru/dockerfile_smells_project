FROM ubuntu:trusty
MAINTAINER Alejandro Villamarin <favm@email.com>

# Suppress dpkg errors
ENV TERM=xterm-256color

# Set mirrors to CZ
RUN sed -i "s/https:\/\/archive./https:\/\/cz.archive./g" /etc/apt/sources.list

# Install node.js
RUN apt-get update && \
    apt-get install curl -y && \
    curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash - && \
    apt-get install -y nodejs

# Copy whole directory to service container. .dockerignore needs to be defined
COPY . /app
WORKDIR /app

# Install app dependencies - globally mocha
RUN npm install -g mocha && \
    npm install

ENTRYPOINT ["mocha"]