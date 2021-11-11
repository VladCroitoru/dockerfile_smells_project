FROM debian:latest

LABEL maintainer="docker@irespaldiza.com" 
LABEL version: "1.0"

RUN  apt-get update && apt install --no-install-recommends -y -qq \
     apt-transport-https \
     ca-certificates \
     curl \
     gnupg2 \
     vim \
     git \
     software-properties-common

RUN curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg | apt-key add -

RUN add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
   $(lsb_release -cs) \
   stable"

RUN apt update && apt install -y -qq docker-ce && \
    rm -rf /var/lib/apt/lists/*

RUN curl -L https://github.com/docker/compose/releases/download/1.16.1/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose && chmod +x /usr/local/bin/docker-compose

WORKDIR /root
