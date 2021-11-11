FROM ubuntu:latest
MAINTAINER Yukimitsu Yabuki, yukimitsu.yabuki@gmail.com
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get -y update \
    && apt-get -y install wget \
    && apt-get -y install software-properties-common \
    && add-apt-repository -y ppa:george-edison55/cmake-3.x \
    && apt-get -y install cmake \
    && apt-get -y install libboost-all-dev \
    && apt-get -y install libtbb-dev \
    && apt-get -y install g++ \
    && apt-get -y install zlib1g-dev \
    && apt-get -y install dialog \
    && apt-get -y install curl \
    && apt-get -y install unzip \
    && apt-get -y install autoconf \
    && apt-get -y upgrade \
    && wget -O sailfish.tar.gz https://github.com/kingsfordgroup/sailfish/archive/v0.10.0.tar.gz \
    && tar xvfz sailfish.tar.gz \
    && mkdir sailfish \
    && cd sailfish \
    && mkdir build \
    && cd build \
    && CXX=g++ cmake -DBOOST_ROOT=/usr/local -DTBB_INSTALL_DIR=/usr/local -DCMAKE_INSTALL_PREFIX=/sailfish /sailfish-0.10.0\
    && make \
    && make install \
    && apt-get clean \
    && rm -r /var/lib/apt/lists/*
ENV PATH $PATH:/sailfish/bin
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/sailfish/lib
RUN echo $PATH
RUN echo $LD_LIBRARY_PATH
WORKDIR /sailfish
