FROM centos:7
MAINTAINER Nao Takeuchi <naonao2dx@gmail.com>

RUN yum -y update; yum clean all;
RUN yum -y install gcc-c++
RUN yum -y install wget
RUN yum -y install make

WORKDIR /usr/local/src

RUN wget https://cmake.org/files/v3.11/cmake-3.11.0-Linux-x86_64.tar.gz
RUN tar zxvf cmake-3.11.0-Linux-x86_64.tar.gz
RUN ln -s /usr/local/src/cmake-3.11.0-Linux-x86_64/bin/cmake /usr/local/bin/cmake

WORKDIR /NetworkServer
COPY . .
RUN cmake .
RUN cmake --build ./ --target NetworkServer
RUN mkdir build
RUN mv NetworkServer build/

WORKDIR /NetworkServer/build
#CMD ["./NetworkServer", "Web", "start"]

EXPOSE 8080
