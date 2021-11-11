FROM ubuntu:xenial
MAINTAINER Lenny Maiorani <ldm5180@gmail.com>

RUN apt-get update && apt-get install -y \
  curl python gawk build-essential cmake git \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN cd /usr/local \
  && curl -L http://releases.llvm.org/4.0.0/clang+llvm-4.0.0-x86_64-linux-gnu-ubuntu-16.04.tar.xz | tar --strip-components=1 -xJ

ENV CC=clang CXX=clang++
