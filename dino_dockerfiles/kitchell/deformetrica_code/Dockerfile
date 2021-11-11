FROM nvidia/cuda:8.0-devel-ubuntu16.04
MAINTAINER Michael Bacci <michael.bacci@inria.fr>

## Build-time variables
# --build-arg GITLAB_USER='' --build-arg GITLAB_PSWD='' --build-arg USE_CUDA=ON
ARG ITK_TAG=v4.9.0
ARG VTK_TAG=v7.1.0
ARG GITLAB_USER
ARG GITLAB_PSWD
ARG USE_CUDA=OFF

## Basic Requierements
RUN apt-get update
RUN apt-get install -y \
      build-essential \
      wget \
      unzip \
      git \
      cmake \
      g++-4.8 \
      libboost-all-dev \
      freeglut3-dev \
      libfftw3-dev \
      libopenblas-dev \
      liblapack-dev \
      xz-utils \
      vim

## use /usr/src as base directory for sources
RUN mkdir -p /usr/src/
WORKDIR /usr/src/

## Cloning ITK
RUN git clone https://github.com/Kitware/ITK.git && \
    cd ITK && \
    git checkout $ITK_TAG

## Compile and Install ITK
ENV ITK_HOME /usr/src/ITK
RUN cd ITK && mkdir build && cd build $ITK_HOME && \
    cmake   -D CMAKE_CXX_COMPILER=/usr/bin/g++-4.8 \
            -D CMAKE_SHARED_LIBS=ON \
            -D CMAKE_CXX_FLAGS="-O3 -fPIC" \
            -D USE_FFTWD=ON \
            -D USE_FFTWF=ON \
            -D CMAKE_BUILD_TYPE=RELEASE \
            -D BUILD_EXAMPLES=OFF \
            -D BUILD_TESTING=OFF  ../ && \
    make -j 4 && \
    make install

## Cloning VTK
ENV VTK_HOME /usr/src/VTK
RUN git clone https://github.com/Kitware/VTK.git $VTK_HOME && \
    cd VTK && \
    git checkout $VTK_TAG

## Compile and Install VTK
RUN cd VTK && mkdir build && cd build && \
    cmake   -D CMAKE_CXX_COMPILER=/usr/bin/g++-4.8 \
            -D CMAKE_SHARED_LIBS=ON \
            -D CMAKE_CXX_FLAGS="-O3 -fPIC" \
            -D CMAKE_BUILD_TYPE=RELEASE \
            -D BUILD_EXAMPLES=OFF \
            -D BUILD_TESTING=OFF  ../ && \
    make -j 4 && \
    make install

## Clone and initialize the Deformetrica repository
ENV DEFORMETRICA_HOME /usr/src/deformetrica
#RUN git clone https://$GITLAB_USER:$GITLAB_PSWD@gitlab.icm-institute.org/aramis/deformetrica.git $DEFORMETRICA_HOME
RUN git clone https://gitlab.icm-institute.org/kitchell/deformetrica.git $DEFORMETRICA_HOME
WORKDIR $DEFORMETRICA_HOME
RUN git checkout stable
RUN git submodule init
RUN git submodule update

## Compile and Install Armadillo
RUN tar -xJf extra/armadillo-7.700.0.tar.xz -C /usr/src/
RUN cd /usr/src/armadillo-7.700.0 && mkdir build && cd build && \
    cmake -D CMAKE_CXX_COMPILER=/usr/bin/g++-4.8 ../ && \
    make -j 4 && \
    make install

ENV LIBRARY_PATH=/usr/local/cuda/lib64/stubs:
ENV LD_LIBRARY_PATH /usr/local/nvidia/lib64:/usr/local/nvidia/lib:/usr/local/cuda/lib64/stubs:/usr/local/cuda/lib64:/usr/local/lib:/usr/lib:

## Compile and Install Deformetrica
RUN mkdir build && cd build && \
    cmake   -D CMAKE_CXX_COMPILER=/usr/bin/g++-4.8 \
            -D USE_CUDA:BOOL=$USE_CUDA \
            -D CMAKE_BUILD_TYPE=RELEASE ../ && \
    make -j 4

RUN cd build && \
    make install deformetrica

## Default command
CMD ["/bin/bash"]

## docker useful links:
# https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/
# https://www.digitalocean.com/community/tutorials/docker-explained-using-dockerfiles-to-automate-building-of-images
