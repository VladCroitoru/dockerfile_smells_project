FROM ubuntu:16.04

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    doxygen graphviz \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /data

ENTRYPOINT doxygen .doxygen
