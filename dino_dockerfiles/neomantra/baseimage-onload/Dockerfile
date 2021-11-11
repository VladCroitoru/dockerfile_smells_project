# Dockerfile which installs Solarflare's OpenOnload into Phusion's baseimage.
#
# OpenOnload web page:
#    http://www.openonload.org/
#
# Uses FROM phusion/baseimage, which is based on Ubuntu 14.04:
#    http://phusion.github.io/baseimage-docker/
# 
# To expose the host and onload to this container, run like this:
#
#   docker run --net=host --device=/dev/onload --device=/dev/onload_epoll -it ONLOAD_ENABLED_IMAGE_ID [COMMAND] [ARG...]
#
# NOTE: The host's OpenOnload version must be the same as the container's.
#
# Copyright (c) 2015 neomantra BV
# Released under the MIT License, see LICENSE.txt
#


FROM phusion/baseimage:latest

MAINTAINER Evan Wies <evan@neomantra.net>


# Update and upgrade apt
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get upgrade -y


# Install OpenOnload build dependencies
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    wget coreutils \
    perl autoconf automake libtool tar gcc make net-tools ethtool \
    valgrind libpcap0.8-dev python-dev \
    gcc-multilib libc6-dev-i386


# Onload version and its md5sum
ENV ONLOAD_VERSION 201509
ENV ONLOAD_MD5SUM  b093ea9f3a534c9c9fe9da6c2b6ccb7a


# Download and verify OpenOnload from Solarflare's site
WORKDIR /tmp
RUN wget http://www.openonload.org/download/openonload-$ONLOAD_VERSION.tgz
RUN echo "$ONLOAD_MD5SUM openonload-$ONLOAD_VERSION.tgz" | md5sum --check


# Extract, build, and install onload
RUN tar -zxf openonload-$ONLOAD_VERSION.tgz
WORKDIR /tmp/openonload-$ONLOAD_VERSION/scripts
RUN ./onload_build --user
RUN ./onload_install --userfiles --nobuild


# Cleanup
RUN rm -rf /tmp/openonload-$ONLOAD_VERSION
WORKDIR /
