# docker build . -t 'latex'
# docker run -it --rm latex:latest /bin/bash
# docker run -it --rm -v `pwd`:/scratch latex:latest /bin/bash

# https://hub.docker.com/r/phusion/baseimage/tags
FROM phusion/baseimage:18.04-1.0.0

RUN apt-get update && \
    apt-get install -y \
# download files from the internet
         wget \
# extract compressed files
         zip \
# edit source code
         vim \
         python3 \
         python3-pip \
         python3-dev \
# compile .tex to verify the latex is valid
         texlive


WORKDIR /opt/

RUN apt-get install -y build-essential flex bison

RUN echo "alias python=python3" > /root/.bashrc
#RUN /bin/bash -l /root/.bashrc
