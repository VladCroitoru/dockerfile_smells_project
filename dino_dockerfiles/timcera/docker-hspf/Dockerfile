FROM debian:jessie
MAINTAINER Tim Cera <tim@cerazone.net>

RUN apt-get update -y && \
    apt-get install -y \
        cmake \
        gfortran
RUN apt-get clean 
RUN mkdir /home/hspf ; \
    mkdir /home/hspf/libatc_dev ; \
    mkdir /home/hspf/libatc_dev_build ; \
    mkdir /home/hspf/hspf_dev ; \
    mkdir /home/hspf/hspf_dev_build

# Copy the source code into the container
COPY libatc-dev/devel/ /home/hspf/libatc_dev
COPY hspf-dev/devel/ /home/hspf/hspf_dev

# Required so the hspf executable can find libatc
ENV LD_LIBRARY_PATH /usr/local/lib

# Make and install libatc first
WORKDIR /home/hspf/libatc_dev_build
RUN cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/usr/local \
        ../libatc_dev && \
    make && \
    make install && \
    make clean

# The hspf cmake must find libatc already installed
WORKDIR /home/hspf/hspf_dev_build
RUN cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/usr/local \
        ../hspf_dev && \
    make && \
    make install && \
    make clean

WORKDIR /home/hspf

ENTRYPOINT ["hspf"]

