FROM ubuntu:18.04

RUN apt-get -q -y update

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y locales

RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=en_US.UTF-8

ENV LANG en_US.UTF-8

# For python 
RUN apt-get -q -y install build-essential git gcc nano
RUN apt-get -q -y install libssl-dev libffi-dev python-dev python python-pip python3 python3-pip

# Image and video processing
RUN apt-get install -q -y imagemagick ffmpeg

# For running https://github.com/achiku/planter
RUN apt-get install -q -y golang-go gom
ENV GOPATH="/root/go"
ENV PATH="${PATH}:${GOPATH}"
RUN apt-get install -q- y graphviz openjdk-8-jre
