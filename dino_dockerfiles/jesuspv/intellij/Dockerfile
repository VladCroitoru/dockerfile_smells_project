FROM ubuntu:xenial

MAINTAINER Jesús Pardillo "dev@jesuspardillo.com"

ENV INTELLIJ_URL https://download.jetbrains.com/idea/ideaIC-2017.1.tar.gz

#####################
# gosu Installation #
#####################

# See https://denibertovic.com/posts/handling-permissions-with-docker-volumes

RUN apt-get update && apt-get -y --no-install-recommends install \
    ca-certificates \
    curl

ENV GOSU_VERSION 1.10
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4
RUN curl -o /usr/local/bin/gosu -SL "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture)" \
    && curl -o /usr/local/bin/gosu.asc -SL "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture).asc" \
    && gpg --verify /usr/local/bin/gosu.asc \
    && rm /usr/local/bin/gosu.asc \
    && chmod +x /usr/local/bin/gosu

#########################
# IntelliJ Installation #
#########################

# See https://hub.docker.com/r/psharkey/intellij

# Get the python script required for "add-apt-repository"
# Configure the openjdk repo
RUN apt-get update \
    && apt-get install -y software-properties-common \
    && add-apt-repository ppa:openjdk-r/ppa

# Install OpenJDK 8, X11 libraries, wget, git, and vim
RUN add-apt-repository ppa:webupd8team/java && apt-get update \
    && apt-get install -y \
       libxext-dev libxrender-dev libxtst-dev \
       openjdk-8-jdk \
       wget \
       git \
       vim \
       x11-xserver-utils

RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/*

RUN wget --progress=bar:force $INTELLIJ_URL -O /tmp/intellij.tar.gz \
    && mkdir -p /opt/intellij \
    && tar xzf /tmp/intellij.tar.gz -C /opt/intellij --strip-components=1 \
    && rm -rf /tmp/*

########################
# Entrypoint with gosu #
########################

COPY entrypoint.sh /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["/opt/intellij/bin/idea.sh"]
