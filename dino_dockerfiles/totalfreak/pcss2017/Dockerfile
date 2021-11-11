#FROM lamtev/cxx
FROM gcc:6.4
#FROM patricol/sfml
FROM tonipes/sfml-docker
FROM rikorose/gcc-cmake
FROM ubuntu:14.04

#ENV CC /usr/local/bin/gcc
#ENV CXX /usr/local/bin/g++

RUN apt-get update && apt-get install -y \
    build-essential \
#    cmake \
    wget \
    git \
#    gcc \
    clang \
#    g++ \
    libegl1-mesa \
    libgl1-mesa-dev \
    libglu1-mesa \
    libglu1-mesa-dev \
    libsfml-dev \
    libgtest-dev \
    binutils-dev \
    libtool \
    lua5.2 \
    liblua5.2-dev \
    liblua5.2-0 \
    graphviz \
    doxygen \
    xvfb
#run apt-get update
#run apt-get install gcc
RUN wget http://www.cmake.org/files/v3.6/cmake-3.6.2.tar.gz

RUN tar -xvf cmake-3.6.2.tar.gz

RUN apt install gcc

#ENV CC /usr/local/bin/gcc
#ENV CXX /usr/local/bin/g++

RUN cd cmake-3.6.2 && \
    ./bootstrap && \
    make && \
    make install

RUN apt install -y dialog

ENV TERM linux
ENV DEBIAN_FRONTEND noninteractive


# runtime dependencies and basic building setup
#run apt update \
run apt upgrade -y \
    && apt install -y \
        build-essential \
#        g++ \
#        cmake \
        git \
        libfreetype6 \
        libjpeg8 \
        xorg \
        libxrandr2 \
        xcb \
        libx11-xcb1 \
        libxcb-randr0 \
        libxcb-image0 \
        libgl1-mesa-glx \
        libflac8 \
        libogg0 \
        libvorbis0a \
        libvorbisenc2 \
        libopenal1 \
        libudev1


 #Replace 1000 with your user / group id
RUN export uid=1000 gid=1000 && \
    mkdir -p /home/developer && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    chown ${uid}:${gid} -R /home/developer

USER developer
ENV HOME /home/developer

ENV DISPLAY 1.0
ADD . /executable
WORKDIR /executable
RUN sudo cmake .
RUN sudo make
RUN chmod +x clientExe
RUN echo $DISPLAY
#RUN ./clientExe