FROM shippableimages/ubuntu1404_base
MAINTAINER Florian Loch (florian.loch@gmail.com)
RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install build-essential -y && \
  apt-get install wget -y && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN mkdir /opt/cmake
RUN cd /opt/cmake && \
  wget https://cmake.org/files/v3.4/cmake-3.4.1.tar.gz && \
  tar xf cmake-3.4.1.tar.gz && \
  cd cmake-3.4.1 && \
  ./configure && \
  make && \
  make install && \
  rm /opt/cmake/cmake-3.4.1.tar.gz
