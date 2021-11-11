FROM ubuntu:latest

RUN apt-get -y update
RUN apt-get install -y wget make build-essential checkinstall libgflags-dev libsnappy-dev zlib1g-dev libbz2-dev git \
    && apt-get clean
RUN mkdir /build \
    && cd /build \
    && git clone https://github.com/facebook/rocksdb.git \
    && cd rocksdb \
    && INSTALL_PATH=/usr make install-shared \
    && rm -rf /build
