################################################################################
# Base image
################################################################################

FROM ubuntu:16.04

################################################################################
# Environment variables
################################################################################

ENV ICECAST_VERSION 2.4.3
ENV ICECAST_SOURCE http://downloads.xiph.org/releases/icecast

################################################################################
# Build instructions
################################################################################

USER root

RUN apt-get -qq update
RUN apt-get -qq install -y \
  make \
  curl \
  automake \
  libtool \
  libxslt-dev \
  libogg-dev \
  libvorbis-dev \
  openssl \
  supervisor \
  git-core

WORKDIR /

RUN curl -sL $ICECAST_SOURCE/icecast-$ICECAST_VERSION.tar.gz \
  | tar xz

RUN mv icecast-$ICECAST_VERSION icecast

WORKDIR /icecast

RUN ./configure && make && make install

COPY entrypoint.sh ./
COPY icecast.xml ./
COPY supervisord.conf ./
COPY app ./app

################################################################################
# Entrypoint
################################################################################

ENTRYPOINT ["./entrypoint.sh"]
