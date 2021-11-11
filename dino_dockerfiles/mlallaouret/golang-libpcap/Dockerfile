FROM golang:1.6

MAINTAINER Marc Lallaouret <mlallaouret@gmail.com> 

RUN apt-get update \
    && apt-get install flex bison -y \
    && apt-get clean

RUN wget http://www.tcpdump.org/release/libpcap-1.7.4.tar.gz && tar xzf libpcap-1.7.4.tar.gz \
    && cd libpcap-1.7.4 \
    && ./configure && make install
