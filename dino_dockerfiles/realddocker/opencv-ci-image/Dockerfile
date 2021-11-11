# A Ubuntu 16.04 image with opencv.
FROM        ubuntu:16.04
MAINTAINER Mark Sheehan


run     apt-get update

# clang and cppcheck have been added perform code quality checks.
RUN apt-get update && \
        apt-get install -y \
        build-essential \
        cmake \
        git \
        wget \
        unzip \
        yasm \
        pkg-config \
        libswscale-dev \
        libtbb2 \
        libtbb-dev \
        libjpeg-dev \
        libpng-dev \
        libtiff-dev \
        libjasper-dev \
        libavformat-dev \
        libpq-dev \
        clang \
        cppcheck 

run     apt-get install -y -q libavformat-dev libavcodec-dev libavfilter-dev libswscale-dev
run     apt-get install -y -q libjpeg-dev libpng-dev libtiff-dev libjasper-dev zlib1g-dev libopenexr-dev libeigen3-dev libtbb-dev
run wget -q https://github.com/opencv/opencv/archive/3.3.1.zip
run unzip -q 3.3.1.zip
run mkdir opencvbuild
run cd opencvbuild && cmake ../opencv-3.3.1/
run cd opencvbuild && make
