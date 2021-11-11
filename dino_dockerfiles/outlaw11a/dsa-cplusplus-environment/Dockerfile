FROM ubuntu

RUN echo "deb http://archive.ubuntu.com/ubuntu/ trusty universe" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get -y install g++-4.4
RUN ln -s /usr/bin/g++-4.4 /usr/bin/g++
RUN apt-get -y install make
RUN apt-get -y install cxxtest
