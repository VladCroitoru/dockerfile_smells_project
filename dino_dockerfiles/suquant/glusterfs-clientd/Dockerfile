FROM ubuntu:xenial
MAINTAINER George Kutsurua <g.kutsurua@gmail.com>

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y glusterfs-client && \
    apt-get clean && \
    apt-get autoclean
