FROM ubuntu:16.04

WORKDIR /root/src/

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
    libtiff-dev && \
    wget https://jaist.dl.sourceforge.net/project/opencvlibrary/opencv-unix/2.4.13/opencv-2.4.13.zip && \
    unzip opencv-2.4.13.zip && \
    cd opencv-2.4.13/ && \
    mkdir build && \
    cd build && \
    cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_TBB=ON .. && \
    make -j$(nproc) && make install -j$(nproc) && \
    cd ../.. && \
    rm opencv-2.4.13.zip && \
    wget http://svnext.it-sudparis.eu/svnview2-eph/ref_syst/Iris_Osiris_v4.1/download/Iris_Osiris_v4.1.tar.gz && \
    tar xzvf Iris_Osiris_v4.1.tar.gz && \
    cd Iris_Osiris_v4.1/src/ && \
    make && \
    cd ../.. && \
    rm Iris_Osiris_v4.1.tar.gz && \
    ln -s /root/src/Iris_Osiris_v4.1 /OSIRIS

ENV LD_LIBRARY_PATH /usr/local/lib:$LD_LIBRARY_PATH
