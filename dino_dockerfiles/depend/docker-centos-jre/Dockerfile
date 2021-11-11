FROM centos:latest
MAINTAINER Nathon Fowlie <nathon.fowlie@gmail.com>

WORKDIR /tmp

COPY install.sh install.sh

RUN chmod a+x install.sh && \
    /bin/bash ./install.sh -v 8u141 -k 336fa29ff2bb4ef291e347e091f7f4a7
