FROM library/ubuntu:16.04

MAINTAINER Mauricio Villegas <mauricio_ville@yahoo.com>

ENV DEBIAN_FRONTEND=noninteractive


### Copy the source code to a temporal directory ###
COPY . /tmp/textFeats/


### Install build pre-requisites ###
RUN apt-get update --fix-missing \
 && apt-get install -y --no-install-recommends \
      build-essential \
      cmake \
      libxml2-dev \
      libxslt1-dev \
      libopencv-dev \
      libmagick++-dev \
      libconfig++-dev \
      libhdf5-dev \


### Compile and install tesseract-recognize ###
 && cd /tmp/textFeats \
 && cmake -DCMAKE_BUILD_TYPE=Release . \
 && make install install-docker \


### Remove build-only software and install runtime pre-requisites ###
 && cd \
 && rm -rf /tmp/textFeats \
 && apt-get purge -y \
      build-essential \
      cmake \
      libxml2-dev \
      libxslt1-dev \
      libopencv-dev \
      libmagick++-dev \
      libconfig++-dev \
      libhdf5-dev \
 && apt-get autoremove -y \
 && apt-get purge -y $(dpkg -l | awk '{if($1=="rc")print $2}') \
 && apt-get install -y --no-install-recommends \
      libxml2 \
      libxslt1.1 \
      libopencv-flann2.4v5 \
      libopencv-highgui2.4v5 \
      libopencv-imgproc2.4v5 \
      libmagick++-6.q16-5v5 \
      libconfig++9v5 \
      libhdf5-cpp-11 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
