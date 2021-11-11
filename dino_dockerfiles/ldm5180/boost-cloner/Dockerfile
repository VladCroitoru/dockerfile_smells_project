FROM ubuntu:latest
MAINTAINER Lenny Maiorani <ldm5180@gmail.com>

RUN apt-get update && apt-get install -y \
  git \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN git clone --recursive --branch boost-1.67.0 https://github.com/boostorg/boost.git
