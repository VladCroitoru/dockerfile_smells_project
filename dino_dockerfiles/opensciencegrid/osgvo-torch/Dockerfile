FROM ubuntu:16.04

MAINTAINER Mats Rynge <rynge@isi.edu>


RUN apt-get update && apt-get upgrade -y --allow-unauthenticated

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get install -y --allow-unauthenticated \
        build-essential \
        cmake \
        curl \
        g++ \
        gcc \
        gdb \
        gfortran \
        git \
        git-core \
        gnuplot \
        gnuplot-x11 \
        imagemagick \
        ipython \
        libfftw3-dev \
        libgraphicsmagick1-dev \
        libjpeg-dev \
        libopenblas-base \
        libopenblas-dev \
        libpng-dev \
        libqt4-dev \
        libreadline-dev \
        libsox-dev \
        libsox-fmt-all \
        libssl-dev \
        libzmq3-dev \
        ncurses-dev \
        python-dev \
        python-pip \
        python-zmq \
        software-properties-common \
        sox \
        strace \
        sudo \
        unzip \
        wget \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Jupyter Notebook for iTorch
RUN pip install --upgrade pip
RUN pip install --upgrade jupyter

RUN mkdir -p /opt/torch

# Torch7 installation scripts - http://torch.ch/docs/getting-started.html
RUN git clone https://github.com/torch/distro.git /opt/torch --recursive && \
    cd /opt/torch && \
    bash install-deps && \
    cp pkg/torch/lib/TH/cmake/FindSSE.cmake pkg/torch/lib/TH/cmake/FindSSE.cmake.ORIG && \
    perl -p -i -e 's/^CHECK_SSE.*//' pkg/torch/lib/TH/cmake/FindSSE.cmake && \
    (diff -u pkg/torch/lib/TH/cmake/FindSSE.cmake.ORIG pkg/torch/lib/TH/cmake/FindSSE.cmake || true) && \
    ./install.sh

COPY .singularity.d /.singularity.d

# some extra singularity stuff
RUN cd / && \
    ln -s .singularity.d/actions/exec .exec && \
    ln -s .singularity.d/actions/run .run && \
    ln -s .singularity.d/actions/test .shell && \
    ln -s .singularity.d/runscript singularity

# build info
RUN echo "Timestamp:" `date --utc` | tee /image-build-info.txt

