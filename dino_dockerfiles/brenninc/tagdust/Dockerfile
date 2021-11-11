FROM ubuntu:14.04

MAINTAINER Christian Brenninkmeijer <Christian.Brenninkmeijer@manchester.ac.uk>

RUN apt-get update

RUN apt-get install -y --force-yes \
    cpp-4.6 \
    curl \
    gcc-4.6-base \ 
    libc6-dev \
    libgomp1 \
    libquadmath0 \
    make \
    pkg-config \
    zlib1g-dev 

#NOTE: This method of install is designed to mimic how galaxy installs rather than the best general install method.
RUN curl -L  http://sourceforge.net/projects/tagdust/files/tagdust-2.13.tar.gz > tagdust-2.13.tar.gz && \
    tar xzf tagdust-2.13.tar.gz && \
    rm tagdust-2.13.tar.gz && \
    cd tagdust-2.13 && \
    ./configure && \
    make && \
    cd / && \
    mv /tagdust-2.13/src /mytagdust && \
    rm -r /tagdust-2.13 

ENV PATH /mytagdust:$PATH



