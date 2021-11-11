# Generic CI Build Image for Amazon Lambda (Node Environment)
#
# https://github.com/flyandi/ci-build-image-aws-lambda-node
# Maintained by Andy Schwarz <flyandi@yahoo.com>
# 
# This docker image is intended to provide a lightweight but still feature-rich 
# build image for Amazon Lambda Functions. The image includes several standard 
# system packages, node and the Amazon Command Line Tool.
#
# Its mainly used for continues integration build jobs.
#
# - Current Lambda Node Runtime (4.3.2)
# - Latest AWSCLI 
# - System packages like wget, jq, zip, unzip, curl, ssh, git, etc.
# - Bonus: Docker
#

FROM debian:jessie
MAINTAINER Andy Schwarz <flyandi@yahoo.com>

# @import packages
RUN \
    apt-get update \
    && apt-get install -y --no-install-recommends \
    ssh \
    curl \
    git \
    vim \
    wget \
    zlib1g-dev \
    jq \
    build-essential \
    iptables \
    libapparmor1 \
    libltdl7 \
    libmcrypt-dev \
    libxml2-dev \
    zip \
    unzip \
    python \
    python-pip \
    python-yaml \
    && apt-get clean

# @import node
RUN \
    curl https://apt.dockerproject.org/repo/pool/main/d/docker-engine/docker-engine_1.13.0-0~debian-jessie_amd64.deb > /tmp/docker.deb \
    && dpkg -i /tmp/docker.deb

# @import awscli
RUN pip install awscli

# @import node
ENV NPM_CONFIG_LOGLEVEL=info
ENV NODE_VERSION=4.3.2
RUN \
  set -ex \
  && for key in \
    9554F04D7259F04124DE6B476D5A82AC7E37093B \
    94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
    0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \
    FD3A5288F042B6850C66B31F09FE44734EB7990E \
    71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
    DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
    B9AE9905FFD7803F25714661B63B535A4C206CA9 \
    C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
  ; do \
    gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
  done \
  && curl -sSLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz" \
  && curl -sSLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
  && gpg --verify SHASUMS256.txt.asc \
  && grep "node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc | sha256sum -c - \
  && tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local --strip-components=1 \
  && rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc

#eof
