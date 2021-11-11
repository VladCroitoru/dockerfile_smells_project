FROM ubuntu:14.04

# Install packer
RUN apt-get update \
  && apt-get install -y \
    unzip \
    wget \
    python \
    python-requests \
    python-boto \
    curl \
    make \
  && rm -rf /tmp/packer \
  && mkdir -p /tmp/packer \
  && cd /tmp/packer \
  && wget https://releases.hashicorp.com/packer/1.1.0/packer_1.1.0_linux_amd64.zip \
  && unzip packer_1.1.0_linux_amd64.zip \
  && rm packer_1.1.0_linux_amd64.zip \
  && mv packer* /usr/local/bin/

# Install docker binary
ENV DOCKER_BUCKET get.docker.com
ENV DOCKER_VERSION 1.13.0
ENV DOCKER_SHA256 fc194bb95640b1396283e5b23b5ff9d1b69a5e418b5b3d774f303a7642162ad6

RUN set -x \
	&& curl -fSL "https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-$DOCKER_VERSION.tgz" -o docker.tgz \
	&& echo "${DOCKER_SHA256} *docker.tgz" | sha256sum -c - \
	&& tar -xzvf docker.tgz \
	&& mv docker/* /usr/local/bin/ \
	&& rmdir docker \
	&& rm docker.tgz \
	&& docker -v

# Cleanup
RUN apt-get clean autoclean \
  && apt-get autoremove -y --purge \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
  && rm -rf /var/lib/{apt,dpkg,cache,log}/ \
  && mkdir -p /src

WORKDIR /src