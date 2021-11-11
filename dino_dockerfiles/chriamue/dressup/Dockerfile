FROM nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04

RUN apt-get update && apt-get install -y \
      build-essential \
      cmake \
      git \
      rpm \
      libatlas-base-dev \
      libatlas-dev \
      libboost-all-dev \
      libgflags-dev \
      libgoogle-glog-dev \
      libhdf5-dev \
      libleveldb-dev \
      liblmdb-dev \
      libopencv-dev \
      libprotobuf-dev \
      libsnappy-dev \
      lsb-release \
      protobuf-compiler \
      python-dev \
      python-numpy \
      python-pip \
      python-setuptools \
      python-scipy \
      sudo \
      wget \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip

RUN git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose \
    && cd openpose && mkdir -p build && cd build \
    && cmake .. && make -j"$(nproc)"

RUN cd openpose/build && make install

RUN git clone https://github.com/gflags/gflags.git \
    && cd gflags && mkdir -p build && cd build \
    && cmake .. && make -j"$(nproc)" && make install

# ADD . /dressup
# RUN cd dressup && mkdir build && cd build && cmake .. && make

RUN cd / && git clone https://github.com/chriamue/dressup.git && cd dressup && mkdir build && cd build && cmake -DOpenPose=/openpose/build/cmake .. && make

WORKDIR /dressup/build

CMD ./dressup
