FROM ubuntu:16.04

WORKDIR /root/src/

ENV LD_LIBRARY_PATH /usr/local/lib:$LD_LIBRARY_PATH
ENV PATH /opt/conda/bin:$PATH

RUN apt-get update && \
    apt-get install -y \
    unzip \
    wget \
    build-essential \
    cmake \
    pkg-config \
    libswscale-dev \
    libtbb2 \
    libtbb-dev \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    git && \
    wget https://jaist.dl.sourceforge.net/project/opencvlibrary/opencv-unix/2.4.13/opencv-2.4.13.zip && \
    unzip opencv-2.4.13.zip && \
    cd opencv-2.4.13/ && \
    mkdir build && \
    cd build && \
    cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_TBB=ON .. && \
    make -j$(nproc) && make install -j$(nproc) && \
    cd ../.. && \
    rm opencv-2.4.13.zip && \
    wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh && \
    bash Miniconda2-latest-Linux-x86_64.sh -b -p /opt/conda && \
    conda update -y conda && \
    conda update -n root conda && \
    conda config --set show_channel_urls True && \
    conda config --add channels defaults && \
    conda config --add channels https://www.idiap.ch/software/bob/conda && \
    conda install -y bob && \
    git clone https://gitlab.idiap.ch/bob/antispoofing.optflow.git && \
    cd antispoofing.optflow && \
    python setup.py install && \
    cd .. && \
    rm -f Miniconda2-latest-Linux-x86_64.sh && \
    rm -rf antispoofing.optflow && \
    rm -rf /opt/conda/pkgs/*
