FROM ubuntu:16.04
MAINTAINER ttsurumi@nefrock.com

# https://github.com/BVLC/caffe/wiki/Ubuntu-16.04-or-15.10-Installation-Guide#the-gpu-support-prerequisites
RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    git \
    zip \
    wget \
    curl \
    ffmpeg \
    pkg-config \
    qtbase5-dev \
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
    python3-dev \
    python3-tk\
    python3-pip \
    python3-setuptools \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get install -y \
    gfortran \
    libatlas-dev \
    libavcodec-dev \
    libavformat-dev \
    libboost-all-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    libswscale-dev \
    pkg-config \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# https://github.com/BVLC/caffe/wiki/OpenCV-3.1-Installation-Guide-on-Ubuntu-16.04
RUN apt-get install --assume-yes \
    libdc1394-22 \
    libdc1394-22-dev \
    libpng12-dev \
    libtiff5-dev \
    libjasper-dev


RUN pip3 install --upgrade pip
RUN pip3 install numpy scipy


WORKDIR /workspace

# install opencv
RUN cd ~ && \
    mkdir -p ocv-tmp && \
    cd ocv-tmp && \
    curl -L https://github.com/opencv/opencv/archive/3.2.0.tar.gz -o ocv.tgz && \
    tar -zxvf ocv.tgz && \
    cd opencv-3.2.0 && \
    mkdir build && \
    cd build && \
    cmake -D CMAKE_BUILD_TYPE=RELEASE \
          -D CMAKE_INSTALL_PREFIX=/usr/local \
          -D BUILD_PYTHON_SUPPORT=ON \
          -D WITH_TBB=ON \
          -D WITH_V4L=ON \
          -D WITH_QT=ON \
          -D WITH_OPENGL=ON \
          .. && \
    make -j8 && \
    make install && \
    /bin/bash -c 'echo "/usr/local/lib" > /etc/ld.so.conf.d/opencv.conf' && \
    ldconfig && \
    apt-get update && \
    rm -rf ~/ocv-tmp

# install dlib
RUN cd ~ && \
    mkdir -p dlib-tmp && \
    cd dlib-tmp && \
    curl -L \
         https://github.com/davisking/dlib/archive/v19.4.tar.gz -o dlib.tar.gz && \
    tar zxvf dlib.tar.gz && \
    cd dlib-19.4/examples && \
    mkdir build && \
    cd build && \
    cmake .. && \
    cmake --build .  && \
    cd ../../ && \
    python3 setup.py install

RUN apt-get install -y libopenblas-dev swig

WORKDIR /root