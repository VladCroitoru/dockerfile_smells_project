FROM ubuntu:14.04
MAINTAINER Tim Head <betatim@gmail.com>

# Taken from the jupyter/notebook Dockerfile
# https://hub.docker.com/r/jupyter/notebook/
#
# Not essential, but wise to set the lang
# Note: Users with other languages should set this in their derivative image
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV PYTHONIOENCODING UTF-8

# Remove preinstalled copy of python that blocks our ability to install development python.
RUN DEBIAN_FRONTEND=noninteractive apt-get remove -yq \
        python3-minimal \
        python3.4 \
        python3.4-minimal \
        libpython3-stdlib \
        libpython3.4-stdlib \
        libpython3.4-minimal

# Python binary and source dependencies
RUN apt-get update -qq && \
    DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
        build-essential \
        ca-certificates \
        curl \
        git \
        language-pack-en \
        libboost-all-dev \
        libcurl4-openssl-dev \
        libexpat1-dev\
        libffi-dev \
        libgl1-mesa-dev \
        libmotif-dev \
        libsqlite3-dev \
        libx11-dev \
        libxerces-c-dev \
        python \
        python3 \
        python-dev \
        python3-dev \
        sqlite3 \
        xorg \
        xorg-dev \
        zlib1g-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install the recent pip release
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \
    python2 get-pip.py && \
    python3 get-pip.py && \
    rm get-pip.py && \
    pip2 --no-cache-dir install requests[security] && \
    pip3 --no-cache-dir install requests[security]

# CMake 3.3
RUN cd /tmp/ && \
    curl -O https://cmake.org/files/v3.3/cmake-3.3.2.tar.gz && \
    tar xzf cmake-3.3.2.tar.gz && \
    cd cmake-3.3.2 && \
    ./configure && \
    make && \
    make install && \
    cd /tmp && \
    rm -rf /tmp/cmake-3.3.2

# Install Geant4
# OpenGL_X11 is needed to make the python bindings work
RUN mkdir -p ~/GEANT4/source && \
    mkdir ~/GEANT4/build && \
    cd ~/GEANT4/source && \
    curl -O http://geant4.cern.ch/support/source/geant4.10.02.tar.gz && \
    tar -xzf geant4.10.02.tar.gz && \
      cd ../build && \
      cmake ~/GEANT4/source/geant4.10.02 -DGEANT4_USE_OPENGL_X11=ON -DGEANT4_INSTALL_DATA=ON && \
      make -j4 && \
      make install && \
    cd ~/GEANT4/source/geant4.10.02/environments/g4py/ && \
      mkdir build && \
      cd build && \
      cmake .. && \
      make && \
      make install && \
      cp -r ~/GEANT4/source/geant4.10.02/environments/g4py/lib/Geant4/ /usr/local/lib/python2.7/dist-packages/ && \
      cp -r ~/GEANT4/source/geant4.10.02/environments/g4py/lib/g4py/ /usr/local/lib/python2.7/dist-packages/ && \
    cd /root && rm -rf GEANT4

WORKDIR /root/
RUN echo "source /usr/local/bin/geant4.sh" > ~/.bashrc

