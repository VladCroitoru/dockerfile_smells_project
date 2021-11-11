## docker-lime-build-kernel-module

FROM centos:latest
MAINTAINER Andrew Krug <andrewkrug@gmail.com> 

RUN yum update -y

RUN mkdir -p /usr/src/kernels

RUN yum install make -y

RUN yum install git -y

WORKDIR /usr/src/kernels

RUN git clone https://github.com/504ensicsLabs/LiME 

WORKDIR /usr/src/kernels/linux

WORKDIR /usr/src/kernels/LiME/src

RUN yum install gcc gcc-c++ kernel-headers kernel-devel kernel-firmware kernel-source -y

RUN mkdir /opt/limemodules

VOLUME ["/opt/limemodules/"]

CMD for KERNS in /usr/src/kernels/*.*.*-*; do make -C $KERNS M=/usr/src/kernels/LiME/src && current="`echo $KERNS | cut -d '/' -f5`" && mv lime.ko /opt/limemodules/$current.ko && echo $current; done
