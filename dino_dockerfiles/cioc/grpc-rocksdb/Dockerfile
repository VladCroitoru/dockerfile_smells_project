FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y build-essential autoconf libtool curl git

RUN git clone -b $(curl -L http://grpc.io/release) https://github.com/grpc/grpc \
    && cd grpc \
    && git submodule update --init \
    && make \
    && make install \
    && cd third_party/protobuf \
    && make \
    && make install

RUN apt-get install -y libgflags-dev libsnappy-dev zlib1g-dev libbz2-dev \
    && git clone https://github.com/facebook/rocksdb.git \
    && cd rocksdb \
    && make shared_lib \
    && make install-shared

RUN mkdir -p /build
COPY Makefile /build
COPY src /build/src

RUN cd /build \
    && make

ENV LD_LIBRARY_PATH usr/lib:/usr/local/lib
