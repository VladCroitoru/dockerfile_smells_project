FROM golang:latest
MAINTAINER Christopher Scott <cscott@axiomzen.co>
ENV REFRESHED_AT 2017-09-07

# curl version
# skipped 7.55.1 due to bug
ENV CURL_VERSION 7.54.1

# Install dependencies
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y \
  build-essential \
  file

WORKDIR /tmp
# download curl source
RUN wget https://curl.haxx.se/download/curl-${CURL_VERSION}.tar.gz
# untar/unzip
RUN tar xfvz curl-${CURL_VERSION}.tar.gz
WORKDIR /tmp/curl-${CURL_VERSION}
# compile static curl binary
# default location is /usr/local/bin/curl
RUN ./configure --disable-shared --enable-static --disable-threaded-resolver CFLAGS='-static -static-libgcc -Wl,-static -lc' && make && make install
# check that it is there and that it is statically linked
RUN ls -al /usr/local/bin/curl && file /usr/local/bin/curl