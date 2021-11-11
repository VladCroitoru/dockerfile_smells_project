FROM nvidia/cuda:8.0-cudnn5-devel

RUN apt update && \
    apt upgrade -y

RUN apt install -y \
    libboost-dev \
    libboost-system-dev \
    libboost-filesystem-dev  \
    libboost-test-dev  \
    libboost-serialization-dev  \
    libboost-regex-dev \
    libboost-program-options-dev \
    git  \
    mercurial  \
    autotools-dev \
    dh-autoreconf \
    cmake && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

ENV EIGEN_PATH /usr/local/include/eigen
ENV DYNET_PATH /usr/local/src/dynet
ENV CUDA_PATH /usr/local/cuda
ENV NMTKIT_PATH /usr/local/src/nmtkit

WORKDIR /usr/local/include
RUN hg clone https://bitbucket.org/eigen/eigen/ $EIGEN_PATH

WORKDIR /usr/local/src/
RUN git clone https://github.com/clab/dynet.git $DYNET_PATH && \
    cd $DYNET_PATH && \
    mkdir build && cd build && \
    cmake .. -DEIGEN3_INCLUDE_DIR=/usr/local/include/eigen/ -DBACKEND=cuda && \
    make && \
    make install && \
    ldconfig && \
    make clean

RUN git clone https://github.com/odanado/nmtkit.git $NMTKIT_PATH && \
    cd $NMTKIT_PATH && \
    git checkout -b remove-dynetcuda remotes/origin/remove-dynetcuda && \
    git submodule init && \
    git submodule update && \
    autoreconf -i && \
    ./configure --with-eigen=$EIGEN_PATH --with-dynet=$DYNET_PATH --with-cuda=$CUDA_PATH && \
    make

