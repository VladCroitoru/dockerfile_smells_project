FROM nvidia/cuda:8.0-devel-ubuntu16.04

MAINTAINER Paolo Galeone

WORKDIR /

RUN apt-get update \
    && apt-get -y install software-properties-common \
    && add-apt-repository -y ppa:ethereum/ethereum -y \
    && apt-get update \
    && apt-get install -y git \
     cmake \
     libcryptopp-dev \
     libleveldb-dev \
     libjsoncpp-dev \
     libjsonrpccpp-dev \
     libboost-all-dev \
     libgmp-dev \
     libreadline-dev \
     libcurl4-gnutls-dev \
     ocl-icd-libopencl1 \
     opencl-headers \
     mesa-common-dev \
     libmicrohttpd-dev \
     build-essential

RUN git clone https://github.com/galeone/cpp-ethereum/ \
    && cd cpp-ethereum \
    && mkdir build \
    && cd build \
    && cmake -DBUNDLE=cudaminer .. \
    && make -j8

COPY start.sh /start.sh
RUN chmod +x /start.sh

ENTRYPOINT ["/start.sh"]
