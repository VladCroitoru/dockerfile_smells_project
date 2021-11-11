# A docker container for a development environment

FROM ubuntu:14.04

EXPOSE 2368

# Replace shell with bash so we can source files
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Set debconf to run non-interactively
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# Install base dependencies
RUN apt-get update && apt-get install -y -q --no-install-recommends \
        apt-transport-https \
        build-essential \
        ca-certificates \
        curl \
        git \
        libssl-dev \
        python \
        rsync \
        software-properties-common \
        wget \
    && rm -rf /var/lib/apt/lists/*

ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 0.10.33

# Install nvm with node and npm
RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.31.6/install.sh | bash \
    && source $NVM_DIR/nvm.sh

RUN echo "cd /app && nvm install && nvm use && npm prune && npm install" >> ~/.bashrc