FROM ubuntu:latest
MAINTAINER Ryan Kurte <ryankurte@gmail.com>
LABEL Description="Docker image for building x86/64 native projects"

# General dependencies and cleanup
RUN apt-get update && apt-get install -y \
  git \
  subversion \
  curl \
  cmake \
  make \
  automake \
  autoconf \
  python-setuptools \
  ninja-build \
  python-dev \
  libtool \
  unzip \
  libffi-dev \
  libssl-dev \
  libusb-1.0.0 \
  libusb-1.0.0-dev \
  software-properties-common \
  gawk \
  genromfs \
  ccache \
  clang \
  build-essential \
  clang \
  python3 \
  python3-dev \
  python3-pip \
  libsodium-dev \
  libzmq3-dev \
  libczmq-dev \
  pkg-config \
  valgrind \
  cppcheck \
  && apt-get clean && rm -rf /var/lib/apt /tmp/* /var/tmp/*
  

# Update PIP & Install useful packages
RUN pip3 install pystache pyyaml

# Set working directory for manually installed components
WORKDIR /root

# Install GoogleTest
RUN git clone --branch release-1.8.1 --depth=1 https://github.com/google/googletest.git \
    && cd googletest && mkdir -p build && cd build \
    && cmake -GNinja .. && ninja install \
    && cd ../.. && rm -rf ./googletest

# Install Golang
RUN curl -O https://storage.googleapis.com/golang/go1.12.4.linux-amd64.tar.gz \
    && tar -C /usr/local -xf go1.12.4.linux-amd64.tar.gz
ENV PATH $PATH:/usr/local/go/bin
RUN mkdir /root/go
ENV GOPATH /root/go

# Install Protobufs
RUN git clone --branch=v3.1.0 --depth=1 https://github.com/google/protobuf.git \
    && cd protobuf \ 
    && ./autogen.sh && ./configure && make -j 4 && make check && make install && ldconfig \
    && cd ./python \
    && python setup.py install \
    && cd ../../ \
    && rm -rf ./protobuf
    
# Install protobuf-c
RUN git clone  --depth=1  https://github.com/protobuf-c/protobuf-c.git \
  && cd protobuf-c \
  && ./autogen.sh \
  && ./configure \
  && make -j && make install \
  && cd ../ \
  && rm -rf ./protobuf-c







