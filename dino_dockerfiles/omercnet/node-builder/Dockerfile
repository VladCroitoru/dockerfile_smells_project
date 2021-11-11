FROM node:6-slim

RUN apt-get update && \
    apt-get install -y git curl bzip2 && \
    npm install -g bower grunt gulp && \
    mkdir /usr/src/app && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
