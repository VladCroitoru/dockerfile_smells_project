FROM centos:7

ENV version 4.0.2

RUN yum update -y && yum install -y build-essential zlib zlib-devel libssl-dev openssl-devel curl && \
    yum group install -y development tools 

RUN cd && \
    curl -O http://download.joedog.org/siege/siege-${version}.tar.gz && \
    tar -xzf siege-${version}.tar.gz && \
    cd siege-${version} && \
    ./configure --with-ssl && \
    make && \
    make install
