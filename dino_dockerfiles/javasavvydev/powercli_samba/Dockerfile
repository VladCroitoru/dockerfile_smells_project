# FROM ubuntu:latest

FROM vmware/powerclicore:ubuntu14.04
MAINTAINER renoufa@vmware.com

RUN apt update -y && \
  apt install smbclient -y &&\
  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
