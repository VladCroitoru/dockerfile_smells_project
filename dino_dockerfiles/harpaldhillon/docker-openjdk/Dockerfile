# openjdk
#
# VERSION: see `TAG`
FROM ubuntu:14.04
MAINTAINER Joao Paulo Dubas "joao.dubas@gmail.com"

# Fake fuse install to allow jdk
# Based on solution in gist by Henrik Muehe
# https://gist.github.com/henrik-muehe/6155333
# For the issue 514 in docker
# https://github.com/dotcloud/docker/issues/514
RUN apt-get -y -qq --force-yes update \
    && apt-get -y -qq install libfuse2 \
    && cd /tmp \
    && apt-get -y -qq download fuse \
    && dpkg-deb -x fuse_* . \
    && dpkg-deb -e fuse_* \
    && rm fuse_*.deb \
    && echo -en '#!/bin/bash\nexit 0\n' > DEBIAN/postinst \
    && dpkg-deb -b . /fuse.deb \
    && dpkg -i /fuse.deb

# instal openjdk and ant
RUN apt-get -y -qq install openjdk-7-jdk ant

# cleanup install
RUN apt-get -y -qq --force-yes clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# system environment variables
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64
