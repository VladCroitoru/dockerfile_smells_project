FROM ubuntu:16.04
MAINTAINER Margriet Palm

RUN apt-get update -y && \
    apt-get install -y cmake libvtk6-dev libboost-filesystem1.58-dev \
                       libboost-iostreams1.58-dev libproj-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
