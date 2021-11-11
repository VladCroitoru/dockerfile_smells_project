FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu16.04

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
        python-setuptools \
        python-scipy && \
    rm -rf /var/lib/apt/lists/*

ENV CAFFE_ROOT=/opt/caffe
WORKDIR $CAFFE_ROOT

RUN apt-get update && apt-get purge -y python-pip && \
    wget https://bootstrap.pypa.io/get-pip.py && \
    python ./get-pip.py && rm -rf ./get-pip.py && \
    apt-get -y install python-pip && \
    rm -rf /var/lib/apt/lists/*

RUN git clone --recursive https://github.com/rbgirshick/py-faster-rcnn.git && \
    cd py-faster-rcnn/caffe-fast-rcnn && pip install --upgrade pip && \
    cd python && for req in $(cat requirements.txt) pydot; do pip install $req; done && cd .. && \
    mkdir build

RUN cd py-faster-rcnn/caffe-fast-rcnn/build && cmake -DUSE_CUDNN=0  .. && make -j"$(nproc)"

ENV PYCAFFE_ROOT $CAFFE_ROOT/python
ENV PYTHONPATH $PYCAFFE_ROOT:$PYTHONPATH
ENV PATH $CAFFE_ROOT/build/tools:$PYCAFFE_ROOT:$PATH
RUN echo "$CAFFE_ROOT/build/lib" >> /etc/ld.so.conf.d/caffe.conf && ldconfig

WORKDIR /workspace

