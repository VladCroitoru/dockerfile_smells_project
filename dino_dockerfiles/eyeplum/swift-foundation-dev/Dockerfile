FROM ubuntu:16.04
MAINTAINER Yan Li<eyeplum@gmail.com>

RUN apt-get update \
    && apt-get install -y \
# dependencies to build swift
      git \
      cmake \
      ninja-build \
      clang \
      python \
      uuid-dev \
      libicu-dev \
      icu-devtools \
      libbsd-dev \
      libedit-dev \
      libxml2-dev \
      libsqlite3-dev \
      swig \
      libpython-dev \
      libncurses5-dev \
      pkg-config \
      libblocksruntime-dev \
      libcurl4-openssl-dev \
# dependencies to build swift-corelibs-libdispatch
      autoconf \
      libtool \
      systemtap-sdt-dev \
# dependencies to debug
      lldb \
      python-six \
# cleanups
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

