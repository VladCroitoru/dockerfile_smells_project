#-------------------------------------------------------------
# - build:
#   docker build -t jupedsim/jpseditor .
# - run:
#   1. socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\"                                                                  
#   2. docker -it -e DISPLAY=<your ip address>  jupedsim/jpseditor
#-------------------------------------------------------------

FROM ubuntu:14.04
 
MAINTAINER Erik Andresen <e.andresen@uni-wuppertal.de>

# install required packages
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    g++ \
    git \
    lcov \
    doxygen \
    qt5-default qttools5-dev-tools \ 
    # python \
    # python-dev \
    # python-pip \
    && apt-get clean

# set environment
ENV HOME /home/jupedsim

# add user
RUN groupadd -r -g 1000 jupedsim && useradd -r -g jupedsim -u 1000 -m jupedsim
USER jupedsim

# install jpscore
RUN mkdir -p /home/jupedsim/workspace
RUN cd /home/jupedsim/workspace \
    && git clone --depth=5 https://gitlab.version.fz-juelich.de/jupedsim/jpseditor.git \
    && cd jpseditor \
    && mkdir -p build \
    && cd build \
    && cmake -D DESIRED_QT_VERSION=5 ..\
    && make


# by default /bin/bash is executed
CMD $HOME/workspace/jpseditor/bin/JPSeditor
