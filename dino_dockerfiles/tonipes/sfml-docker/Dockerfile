#
# Dockerfile for SFML C++ Project building and testing
#

FROM ubuntu:16.10

MAINTAINER Toni Pesola

RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    git \
    gcc \
    clang \
    g++ \
    libegl1-mesa \ 
    libgl1-mesa-dev \
    libglu1-mesa \
    libglu1-mesa-dev \
    libsfml-dev \
    libgtest-dev \
    binutils-dev \
    libtool \
    lua5.2 \
    liblua5.2-dev \
    liblua5.2-0 \
    graphviz \
    doxygen

RUN wget http://www.cmake.org/files/v3.6/cmake-3.6.2.tar.gz

RUN tar -xvf cmake-3.6.2.tar.gz

RUN cd cmake-3.6.2 && \
    ./bootstrap && \
    make && \
    make install

