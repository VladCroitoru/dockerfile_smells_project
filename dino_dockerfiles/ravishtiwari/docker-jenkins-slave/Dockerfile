# Docker-in-Docker Jenkins Slave
#
# See: https://github.com/tehranian/dind-jenkins-slave
# See: https://dantehranian.wordpress.com/2014/10/25/building-docker-images-within-docker-containers-via-jenkins/
#
# Following the best practices outlined in:
#   http://jonathan.bergknoff.com/journal/building-good-docker-images

FROM evarga/jenkins-slave
MAINTAINER Ravish Tiwari <ravishktiwari@hotmail.com>
ENV DEBIAN_FRONTEND noninteractive
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Adapted from: https://registry.hub.docker.com/u/jpetazzo/dind/dockerfile/
# Let's start with some basic stuff.

RUN apt-get update -qq && apt-get install -qqy \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
RUN add-apt-repository \
    #"deb [arch=amd64] https://download.docker.com/linux/ubuntu artful stable"
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable"
# Install Docker from Docker Inc. repositories.
RUN apt-cache madison docker-ce    
RUN apt-get update  && apt-get install -y docker-ce=17.12.0~ce-0~ubuntu && rm -rf /var/lib/apt/lists/*
RUN curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose

# Install JDK 8 (latest edition)
RUN apt-get -q update &&\
    DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--force-confnew" --no-install-recommends software-properties-common &&\
    add-apt-repository -y ppa:openjdk-r/ppa &&\
    apt-get -q update &&\
    DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--force-confnew" --no-install-recommends openjdk-8-jre-headless &&\
    apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f /var/cache/apt/*.bin
RUN apt-get update -q && \
    apt-get install -yq git \
    python-pip groff-base
RUN pip install awscli \
    pip install aws-sam-cli
RUN add-apt-repository ppa:chris-lea/zeromq
RUN apt-get update
RUN apt-get install libzmq3-dbg libzmq3-dev libzmq3 -yq
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libkrb5-dev \
    pkg-config \
    libtool \
    autoconf \
    automake \
    unzip \
    libglib2.0-dev \
    librsvg2-dev
RUN cd /tmp && git clone git://github.com/jedisct1/libsodium.git && cd libsodium && git checkout stable && ./autogen.sh && ./configure && make check && make install && ldconfig
RUN cd /tmp && git clone --depth 1 git://github.com/zeromq/libzmq.git && cd libzmq && ./autogen.sh && ./configure && make && make install && ldconfig
RUN rm /tmp/* -rf

ADD wrapdocker /usr/local/bin/wrapdocker
RUN chmod +x /usr/local/bin/wrapdocker
VOLUME /var/lib/docker

# Make sure that the "jenkins" user from evarga's image is part of the "docker"
# group. Needed to access the docker daemon's unix socket.
RUN usermod -a -G docker jenkins

# place the jenkins slave startup script into the container
ADD jenkins-slave-startup.sh /
CMD ["/jenkins-slave-startup.sh"]
