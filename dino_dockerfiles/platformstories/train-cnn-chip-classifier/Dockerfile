FROM nvidia/cuda:8.0-cudnn5-runtime-ubuntu16.04

MAINTAINER Nikki Aldeborgh <nikki.aldeborgh@digitalglobe.com>

RUN apt-get -y update && apt-get -y \
    install python \
    build-essential \
    libopencv-dev \
    python-opencv \
    python-software-properties \
    software-properties-common \
    ipython \
    python-pip \
    python-scipy \
    python-numpy \
    python-dev \
    vim \
    wget \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install numpy h5py tensorflow-gpu geojson geojsontools sklearn keras==1.2.2

COPY ./bin /
COPY keras.json /root/.keras/keras.json

