FROM node:6-slim
MAINTAINER Yan Fei <sksycribe.yf@gmail.com>

ARG VERSION=3.2.0
ENV NPM_CONFIG_LOGLEVEL info

# Setup npm http only
RUN npm config set strict-ssl false && npm config set registry "http://registry.npmjs.org"

# gitbook install
RUN npm install --global gitbook-cli && gitbook fetch ${VERSION} && \
    npm cache clear && \
    rm -fr /tmp/*

# Java and OpenJDK
RUN apt-get update && \
    apt-get install -y --no-install-recommends openjdk-7-jre-headless && \
    rm -rf /var/lib/apt/lists/*

# Install build essential and utilities
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential protobuf-compiler wget curl procps openssh-client git bzip2

# Install Calibre, and graphviz for plantuml
RUN echo "deb http://http.debian.net/debian jessie-backports main" > /etc/apt/sources.list.d/backports.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends calibre fonts-noto fonts-noto-cjk locales-all graphviz && \
    rm -rf /var/lib/apt/lists/*

# Add plugin for protc-doc-gen
RUN wget http://download.opensuse.org/repositories/home:estan:protoc-gen-doc/Debian_8.0/Release.key && \
    apt-key add - < Release.key && \
    echo 'deb http://download.opensuse.org/repositories/home:/estan:/protoc-gen-doc/Debian_8.0/ /' >> /etc/apt/sources.list.d/protoc-gen-doc.list && \
    apt-get update && apt-get install protoc-gen-doc 

# Install doctoc tool
RUN npm install -g doctoc

RUN java -version && make --version && gitbook --version && protoc --version && doctoc --help
