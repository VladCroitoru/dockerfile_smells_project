#FROM ubuntu:trusty
FROM zerodivide1/docker-novnc

# Set Locale

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN echo deb http://archive.ubuntu.com/ubuntu precise universe multiverse >> /etc/apt/sources.list; \
    apt-get update -qq && apt-get install -y --force-yes \
    curl \
    git \
    g++ \
    autoconf \
    automake \
    build-essential \
    checkinstall \
    cmake \
    pkg-config \
    yasm \
    libtool \
    python2.7 \
    python2.7-dev \
    python-numpy \
    wget \
    libboost-all-dev \
    libeigen3-dev \
    libqt4-dev \
    libqglviewer-dev \
    libpythonqt-dev \
    libglew-dev \
    unzip; \
    apt-get clean

RUN apt-get install -y --force-yes \
    libqt4-dev \
    libqglviewer-dev

RUN apt-get install -y --force-yes \
    libpythonqt-dev libglew-dev;


WORKDIR /usr/local/src
RUN git clone https://github.com/ebenolson/mscomplex-tri.git

WORKDIR /usr/local/src/mscomplex-tri
RUN git submodule update --init

WORKDIR /usr/local/src
RUN mkdir -p build

WORKDIR /usr/local/src/build
RUN cmake -D BUILD_PYMSTRI=ON \
          -D BUILD_VIEWER=ON \
          -D PYTHON_SITE_PACKAGES_INSTALL_DIR=/usr/lib/python2.7 \
          ../mscomplex-tri

RUN make -j4
RUN make install