FROM geographica/gdal2:2.1.2

MAINTAINER Nikki Aldeborgh <nikki.aldeborgh@digitalglobe.com>

RUN apt-get update -y && apt-get install -y \
    software-properties-common \
    python-software-properties \
    build-essential \
    python \
    python-dev \
    python-numpy \
    python-pip \
    python-scipy \
    ipython \
    python-pip \
    vim


ADD ./bin /
