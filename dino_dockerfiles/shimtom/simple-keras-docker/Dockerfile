FROM ubuntu:16.04

MAINTAINER shimtom

ENV LANG C.UTF-8

# Set up Japanese environment
RUN apt-get update && apt-get install -y \
        language-pack-ja \
        && \
    update-locale LANG=ja_JP.UTF-8 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Pick up some TF dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        apt-utils \
        build-essential \
        curl \
        libfreetype6-dev \
        libpng12-dev \
        libzmq3-dev \
        pkg-config \
        python3 \
        python3-dev \
        python3-pip \
        rsync \
        software-properties-common \
        unzip \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/python3 /usr/bin/python

# install python packages
RUN pip3 install --upgrade pip
RUN pip install -U --no-cache-dir setuptools
RUN pip3 --no-cache-dir install \
        setuptools \
        numpy \
        scipy \
        matplotlib \
        seaborn \
        sklearn \
        pandas \
        pillow \
        keras \
        h5py

# install tensorflow
RUN pip3 install tensorflow

# TensorBoard
EXPOSE 6006

CMD ["/bin/bash"]
