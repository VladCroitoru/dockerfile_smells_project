FROM ubuntu:trusty

MAINTAINER Filipe Brandão <fdabrandao@dcc.fc.up.pt>

RUN DEBIAN_FRONTEND=noninteractive apt-get -y dist-upgrade && \
    apt-get -y install software-properties-common && \
    add-apt-repository ppa:fkrull/deadsnakes

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get -y install \
    make \
    g++-4.8 \
    python2.7 \
    python-pip \
    python-dev \
    python3.5 \
    python3-pip \
    python3.5-dev \
    python-virtualenv \
    glpk-utils
