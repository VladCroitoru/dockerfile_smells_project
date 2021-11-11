FROM nvidia/cuda:8.0-cudnn5-runtime-ubuntu16.04

MAINTAINER Till von Ahnen "xoryouyou@gmail.com"

# prevent shell interactions
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

# prepare for pip3
RUN apt-get update
RUN apt-get install python3-pip python3 python3-dev -y

# get the latest pip
RUN pip3 install --upgrade pip

# install everything needed
RUN pip3 install tensorflow-gpu numpy scipy scikit-learn pillow h5py keras

# setup missing locale
RUN locale-gen en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8
