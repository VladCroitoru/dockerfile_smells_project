FROM ubuntu:17.04

RUN apt-get update

RUN apt-get install -y          \
            git                 \
            gcc                 \
            autoconf            \
            automake            \
            pkg-config          \
            make                \
            libtool             \
            libpcre3-dev        \
            libcap-dev          \
            libncurses5-dev     \
            openssl             \
            tcl-dev             \
            expat               \
            flex                \
            hwloc               \
            curl                \
            zlib1g-dev          \
            libcunit1-dev       \
            libevent-dev        \
            libssl-dev          \
            libxml2-dev         \
            libjansson-dev      \
            libjemalloc-dev

RUN useradd -ms /bin/bash scw00

USER scw00
WORKDIR /home/scw00

RUN git clone --depth 1 https://github.com/apache/trafficserver.git
RUN cd trafficserver &&                 \
    git submodule update --depth 1 &&   \
    autoreconf -if &&                   \
    ./configure  --prefix=/home/scw00/run_dir CCASFLAGS='-g -O0' CXXFLAGS='-g -O0' --with-user=scw00 --with-group=scw00 --enable-experimental-plugins&&        \
    make &&                             \
    make install

