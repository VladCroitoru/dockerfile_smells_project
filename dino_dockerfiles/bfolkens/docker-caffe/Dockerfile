FROM nvidia/cuda:7.0-cudnn4-devel

# Install some dep packages

ENV CAFFE_PACKAGES libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libboost-all-dev libhdf5-serial-dev protobuf-compiler gfortran libjpeg62 libfreeimage-dev libopenblas-dev git python-dev python-pip libgoogle-glog-dev libbz2-dev libxml2-dev libxslt-dev libffi-dev libssl-dev libgflags-dev liblmdb-dev python-yaml python-numpy

RUN apt-get update && \
    apt-get install -y git wget build-essential $CAFFE_PACKAGES && \
    apt-get remove -y cmake && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Upgrade CMake

RUN cd /usr/local/src && \
    wget http://www.cmake.org/files/v3.2/cmake-3.2.2.tar.gz && \
    tar xf cmake-3.2.2.tar.gz && \
    cd cmake-3.2.2 && \
    ./configure --prefix=/usr && \
    make && \
    make install && \
    rm -rf /usr/local/src/cmake*

# Install caffe

RUN cd /usr/local/src && \
    git clone https://github.com/BVLC/caffe.git && \
    cd caffe && \
    pip install --upgrade setuptools pip && \
    cat python/requirements.txt | xargs -L 1 pip install --upgrade && \
    echo 'set(BLAS "Open")' >> CMakeLists.txt && \
    mkdir -p build && \
    cd build && \
    cmake .. -DBLAS=Open -DCMAKE_INSTALL_PREFIX=/usr && \
    make -j"$(nproc)" all && \
#    make runtest && \
    make install && \
    rm -rf /usr/local/src/caffe*

# Train test
# ./data/mnist/get_mnist.sh
# ./examples/mnist/create_mnist.sh
# ./examples/mnist/train_lenet.sh
