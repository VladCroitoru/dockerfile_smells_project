FROM node:10-slim
LABEL maintainer="Matthew Hartstonge <matt@mykro.co.nz>" \
      repo="https://github.com/matthewhartstonge/node-docker"

ENV DOCKER_VERSION="17.05.0~ce-0~debian-jessie"
RUN apt-get update \
    && apt-get install -y \
        apt-transport-https \
        ca-certificates \
        g++ \
        make \
        python \
    && apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D \
    && echo "deb https://apt.dockerproject.org/repo debian-jessie main" >> /etc/apt/sources.list.d/docker.list \
    && apt-get update && apt-get install -y \
        docker-engine="${DOCKER_VERSION}" \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
