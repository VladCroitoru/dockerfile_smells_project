FROM        stackbrew/ubuntu:saucy

MAINTAINER Michael Doran michael.doran.808@gmail.com

ENV         DEBIAN_FRONTEND noninteractive
RUN         echo "deb http://archive.ubuntu.com/ubuntu saucy main universe" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get -y install wget
RUN apt-get -y install make autoconf automake libtool
RUN apt-get -y install gcc-4.8 g++-4.8 
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.8 50
RUN update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.8 50

RUN cd /opt && wget http://protobuf.googlecode.com/files/protobuf-2.5.0.tar.gz && tar -xvf protobuf-2.5.0.tar.gz && sleep 10 && cd /opt/protobuf-2.5.0 && ./configure && make && make install

RUN apt-get -y install libjemalloc-dev

RUN apt-get -y install libboost-all-dev

RUN apt-get -y install git

RUN apt-get -y install pkg-config

RUN apt-get install traceroute

RUN cd /opt && git clone https://github.com/keithw/remy.git

RUN cd /opt/remy && ./autogen.sh && ./configure && make && cp /opt/remy/src/rat-runner /tmp && make install 

RUN cd /opt && git clone https://github.com/DORAM014/seed.git
