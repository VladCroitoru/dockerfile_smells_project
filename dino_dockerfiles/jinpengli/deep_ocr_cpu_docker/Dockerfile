FROM ubuntu:14.04
MAINTAINER mr.li.jinpeng@gmail.com

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        cmake \
        git \
        wget \
        libatlas-base-dev \
        libboost-all-dev \
        libgflags-dev \
        libgoogle-glog-dev \
        libhdf5-serial-dev \
        libleveldb-dev \
        liblmdb-dev \
        libopencv-dev \
        libprotobuf-dev \
        libsnappy-dev \
        protobuf-compiler \
        python-dev \
        python-numpy \
        python-pip \
        python-scipy && \
    rm -rf /var/lib/apt/lists/*

ENV CAFFE_ROOT=/opt/caffe
WORKDIR $CAFFE_ROOT

# FIXME: clone a specific git tag and use ARG instead of ENV once DockerHub supports this.
ENV CLONE_TAG=master

RUN git clone -b ${CLONE_TAG} --depth 1 https://github.com/BVLC/caffe.git . && \
    for req in $(cat python/requirements.txt) pydot; do pip install $req; done && \
    mkdir build && cd build && \
    cmake -DCPU_ONLY=1 .. && \
    make -j"$(nproc)"

ENV PYCAFFE_ROOT $CAFFE_ROOT/python
ENV PYTHONPATH $PYCAFFE_ROOT:$PYTHONPATH
ENV PATH $CAFFE_ROOT/build/tools:$PYCAFFE_ROOT:$PATH
RUN echo "$CAFFE_ROOT/build/lib" >> /etc/ld.so.conf.d/caffe.conf && ldconfig

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y libopencv-dev python-opencv

ENV DEEP_OCR_ROOT=/opt/deep_ocr
RUN git clone --recursive https://github.com/JinpengLI/deep_ocr.git $DEEP_OCR_ROOT

ENV PATH $DEEP_OCR_ROOT/bin:$PATH
ENV PYTHONPATH $DEEP_OCR_ROOT/python:$PYTHONPATH

## install PIL
RUN apt-get update && apt-get install -y --no-install-recommends libjpeg-dev libfreetype6 libfreetype6-dev zlib1g-dev
RUN pip install pillow
RUN sudo ln -s /lib/x86_64-linux-gnu/libz.so.1 /lib/
RUN sudo ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so.6 /usr/lib/
RUN sudo ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so.62 /usr/lib/

RUN apt-get install -y python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose
RUN apt-get install -y gfortran
RUN pip install --upgrade pip
ENV WORKSPACE=/workspace
WORKDIR /workspace

