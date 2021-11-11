FROM ubuntu:20.04 AS base

RUN apt-get update && \
  apt-get -y upgrade &&\
  # set noninteractive installation
  export DEBIAN_FRONTEND=noninteractive && \
  #install tzdata package
  apt-get install -y \
    build-essential \
    cmake \
    cpp \
    curl \
    fdkaac \
    ffmpeg \
    gcc \
    git \
    gnuradio-dev \
    gr-osmosdr \
    hackrf \
    libaacs0 \
    libboost-all-dev \
    libcppunit-1.15-0 \
    libcppunit-dev \
    libcurl4 \
    libcurl4-openssl-dev \
    libfdk-aac-dev \
    libfdk-aac1 \
    libgnuradio-osmosdr0.2.0 \
    libgnuradio-uhd3.8.1 \
    libhackrf-dev \
    libhackrf0 \
    liborc-0.4-dev \
    libosmosdr-dev \
    libosmosdr0 \
    libsox-dev \
    libsox3 \
    libsoxr0 \
    libssl-dev \
    libuhd-dev \
    libuhd3.15.0 \
    libusb-1.0-0 \
    libusb-dev \
    libvo-aacenc0 \
    make \
    openssl \
    osmo-sdr \
    sox \
    tzdata && \
  rm -rf /var/lib/apt/lists/*
