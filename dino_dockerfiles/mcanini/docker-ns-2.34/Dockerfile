FROM ubuntu:12.04
MAINTAINER Marco Canini <marco.canini@gmail.com>

# Credits: adapted from http://ns2-ubuntu.blogspot.com/


RUN apt-get update

RUN apt-get -y install build-essential g++ autoconf automake libxmu-dev
RUN apt-get -y install xorg-dev xgraph

RUN apt-get -y install wget

RUN wget -O ns-allinone-2.34.tar.gz "http://downloads.sourceforge.net/project/nsnam/allinone/ns-allinone-2.34/ns-allinone-2.34.tar.gz?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fnsnam%2Ffiles%2Fallinone%2Fns-allinone-2.34%2F&ts=1457162815&use_mirror=netcologne"

RUN tar zxvf ns-allinone-2.34.tar.gz
RUN rm ns-allinone-2.34.tar.gz

WORKDIR /ns-allinone-2.34
RUN sed -i 's/ld -shared/gcc -shared/g' otcl-1.13/configure && \
    sed -i 's/ErlangRandomVariable::ErlangRandomVariable/ErlangRandomVariable/g' ns-2.34/mobile/nakagami.cc && \
    sed -i 's/GammaRandomVariable::GammaRandomVariable/GammaRandomVariable/g' ns-2.34/mobile/nakagami.cc && \
    sed -i 's/GammaRandomVariable::GammaRandomVariable(1/GammaRandomVariable(1/g' ns-2.34/tools/ranvar.cc && \
    sed -i '/#include "wireless-phyExt.h"/a  #include <stddef.h>' ns-2.34/mac/mac-802_11Ext.h

RUN ./install

WORKDIR /root
ENV OTCL_LIB /ns-allinone-2.34/otcl-1.13
ENV NS2_LIB /ns-allinone-2.34/lib
ENV X11_LIB /usr/X11R6/lib
ENV USR_LOCAL_LIB /usr/local/lib
ENV TCL_LIB /ns-allinone-2.34/tcl8.4.18/library
ENV USR_LIB /usr/lib
ENV XGRAPH /ns-allinone-2.34/bin:/ns-allinone-2.34/tcl8.4.18/unix:/ns-allinone-2.34/tk8.4.18/unix
ENV NS /ns-allinone-2.34/ns-2.34/
ENV NAM /ns-allinone-2.34/nam-1.14/
ENV PATH "$PATH:$XGRAPH:$NS:$NAM"
