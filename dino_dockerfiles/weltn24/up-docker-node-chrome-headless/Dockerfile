FROM ubuntu:bionic

MAINTAINER Harry <harald.urban@weltn24.de>
LABEL vendor="WeltN24 Team Rabbit"
LABEL tools="aws git pip chrome node npm yarn"

# Install deps
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    git \
    python-pip \
    python2.7 \
    python2.7-dev \
    groff-base \
    build-essential \
    --no-install-recommends

# Install aws cli
RUN pip install --upgrade pip setuptools
RUN pip install --upgrade awscli

# Get Chrome sources
RUN curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list

# Install Chrome
# https://www.ubuntuupdates.org/ppa/google_chrome?dist=stable
ENV CHROME_VERSION=90.0.4430.85-1

RUN apt-get update && apt-get install -y \
    google-chrome-stable=$CHROME_VERSION \
    --no-install-recommends

# Get yarn sources
RUN curl -sSL https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb [arch=amd64] https://dl.yarnpkg.com/debian/ stable main" > /etc/apt/sources.list.d/yarn.list

# Install yarn
# https://www.ubuntuupdates.org/ppa/yarn?dist=stable
ENV YARN_VERSION=1.22.5-1

RUN apt-get update && apt-get install -y \
    yarn=$YARN_VERSION \
    --no-install-recommends

# Find your desired version here: https://deb.nodesource.com/node_14.x/pool/main/n/nodejs/
# Ubuntu 18 LTS (Bionic) (https://wiki.ubuntu.com/Releases)
ENV NODE_VERSION=14.16.1

RUN curl https://deb.nodesource.com/node_14.x/pool/main/n/nodejs/nodejs_$NODE_VERSION-1nodesource1_amd64.deb > node.deb \
 && dpkg -i node.deb \
 && rm node.deb
