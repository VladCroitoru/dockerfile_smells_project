# Using the Ubuntu BaseImage from Phusion
# http://phusion.github.io/baseimage-docker/
FROM phusion/baseimage:0.9.17

MAINTAINER Ryan Hatfield <ryan@ryan.bio>

# Get Doxygen version 1.8.6-2
RUN apt-get update && \
    apt-get install -y wget build-essential flex bison g++

# Get CMake and Doxygen
RUN mkdir -p /root/downloads && cd /root/downloads && \
    wget https://cmake.org/files/v3.3/cmake-3.3.2-Linux-x86_64.tar.gz && \
    wget https://github.com/doxygen/doxygen/archive/Release_1_8_10.tar.gz && \
    tar -zxvf cmake-3.3.2-Linux-x86_64.tar.gz && \
    tar -zxvf Release_1_8_10.tar.gz

# Alias CMake and build Doxygen
RUN ln -s /root/downloads/cmake*/bin/cmake /usr/local/bin/cmake && \
    cd /root/downloads/doxygen*/ && mkdir build && cd build && \
    cmake -G "Unix Makefiles" .. && make && make install

# Clean up APT when done.
RUN apt-get remove -y build-essential flex bison g++  && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
