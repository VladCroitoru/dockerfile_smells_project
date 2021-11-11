FROM ubuntu:16.04

MAINTAINER John Wu <john.wu@mail.mcgill.ca>

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    apt-get install -y --no-install-recommends make cmake build-essential && \
    apt-get install -y --no-install-recommends nodejs nodejs-legacy npm && \
    apt-get install -y --no-install-recommends apt-utils && \
    apt-get install -y --no-install-recommends libopencv-dev && \
    apt-get install -y --no-install-recommends libgtk2.0-dev && \
    apt-get install -y --no-install-recommends pkg-config && \
    apt-get install -y --no-install-recommends python-numpy python2.7-dev && \
    apt-get install -y --no-install-recommends libavcodec-dev libavformat-dev libswscale-dev && \
    apt-get install -y --no-install-recommends libjpeg-dev libpng12-dev libtiff5-dev libjasper-dev && \
    apt-get install -y --no-install-recommends zip unzip && \
    apt-get install -y --no-install-recommends checkinstall && \
    apt-get install -y --no-install-recommends yasm && \
    apt-get install -y --no-install-recommends libdc1394-22-dev && \
    apt-get install -y --no-install-recommends libxine2 && \
    apt-get install -y --no-install-recommends libgstreamer0.10-dev && \
    apt-get install -y --no-install-recommends libgstreamer-plugins-base0.10-dev && \
    apt-get install -y --no-install-recommends libv4l-dev && \
    apt-get install -y --no-install-recommends libtbb-dev && \
    apt-get install -y --no-install-recommends libgtk2.0-dev && \
    apt-get install -y --no-install-recommends libmp3lame-dev && \
    apt-get install -y --no-install-recommends libopencore-amrnb-dev && \
    apt-get install -y --no-install-recommends libopencore-amrwb-dev && \
    apt-get install -y --no-install-recommends libtheora-dev && \
    apt-get install -y --no-install-recommends libvorbis-dev && \
    apt-get install -y --no-install-recommends libxvidcore-dev && \
    apt-get install -y --no-install-recommends x264 && \
    apt-get install -y --no-install-recommends v4l-utils && \
    apt-get install -y --no-install-recommends qt-sdk && \
    apt-get install -y --no-install-recommends python-pip && \
    pip install --upgrade pip && \
    pip install setuptools && \
    pip install Pillow && \
    apt-get clean && \
    rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* && \

    # Create build folder for external libraries
    mkdir build && cd build && \

    # OpenCV 2.4
    git clone https://github.com/opencv/opencv && \
    cd opencv && \
    git checkout tags/2.4.13 && \
    mkdir release && \
    cd release && \
    cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D BUILD_NEW_PYTHON_SUPPORT=ON -D BUILD_EXAMPLES=OFF .. && \
    make && \
    make install
