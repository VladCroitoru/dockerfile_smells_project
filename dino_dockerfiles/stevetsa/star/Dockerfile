# This is a comment

FROM ubuntu:latest
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
MAINTAINER Steve Tsang <mylagimail2004@yahoo.com>
RUN apt-get update

RUN apt-get install --yes \
 build-essential \
 gcc-multilib \
 apt-utils \
 zlib1g-dev \
 vim-common

RUN apt-get install -y git

# Get latest STAR source from releases
# Alternatively, get STAR source using git
RUN git clone https://github.com/stevetsa/STAR.git
WORKDIR /STAR/source/

# Build STAR
#RUN pwd
RUN make STARlong

# To include STAR-Fusion
RUN git submodule update --init --recursive

# If you have a TeX environment, you may like to build the documentation
# make manual
ENV PATH /STAR/source:$PATH
WORKDIR /
