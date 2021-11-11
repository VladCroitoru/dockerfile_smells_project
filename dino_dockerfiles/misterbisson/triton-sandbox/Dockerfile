FROM ubuntu:16.04

# Get some packages, Docker, and Docker Compose
RUN set -ex \
    && apt-get update && apt-get install -y --no-install-recommends \
        apt-transport-https \
        ca-certificates \
        curl \
        dnsutils \
        git \
        htop \
        less \
        nodejs \
        npm \
        ssh \
        unzip \
        vim \
    && rm -rf /var/lib/apt/lists/* \
    && ln -s /usr/bin/nodejs /usr/bin/node \
    && npm install -g triton manta json \
    && curl -o /usr/local/bin/triton-docker https://raw.githubusercontent.com/joyent/triton-docker-cli/master/triton-docker \
    && chmod +x /usr/local/bin/triton-docker \
    && ln -Fs /usr/local/bin/triton-docker /usr/local/bin/triton-compose \
    && ln -Fs /usr/local/bin/triton-docker /usr/local/bin/triton-docker-install
    && ln -Fs /usr/local/bin/triton-docker-helper /usr/local/bin/docker \
    && ln -Fs /usr/local/bin/triton-compose-helper /usr/local/bin/docker-compose

WORKDIR /demo

# Build meta and Docker labels
ARG BUILD_DATE
ARG BRANCH
LABEL com.joyent.build-date=$BUILD_DATE \
    com.joyent.branch=$BRANCH

# On macOS, with SSH keys and a Triton config in expected places
# docker run --rm -it -v ~/.ssh:/root/.ssh -v ~/.triton:/root/.triton triton-sandbox bash

