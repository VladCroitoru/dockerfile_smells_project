FROM ubuntu:16.04

MAINTAINER Greg Keys <gregkeys@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
ENV DOCKER_MACHINE 0.9.0
ENV DOCKER_COMPOSE 1.11.2

# Install system packages
RUN apt-get update -q \
    && apt-get -y -q install --no-install-recommends \
            curl \
            ca-certificates \
    && curl -L https://github.com/docker/machine/releases/download/v${DOCKER_MACHINE}/docker-machine-`uname -s`-`uname -m` > /usr/local/bin/docker-machine \
    && chmod +x /usr/local/bin/docker-machine \
    && curl -L https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE}/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose