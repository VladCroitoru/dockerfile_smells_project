FROM ubuntu:xenial
MAINTAINER David Spencer <dspencer@wustl.edu>

LABEL \
  version="v2.4.2" \
  description="Varscan image for use in Workflows"

RUN apt-get update -y && apt-get install -y \
    wget \
    git \
    unzip \
    bzip2 \
    g++ \
    make \
    zlib1g-dev \
    ncurses-dev \
    rsync \
    default-jdk \
    default-jre
    
ENV VARSCAN_INSTALL_DIR=/opt/varscan

WORKDIR $VARSCAN_INSTALL_DIR
RUN wget https://github.com/dkoboldt/varscan/releases/download/2.4.2/VarScan.v2.4.2.jar && \
  ln -s VarScan.v2.4.2.jar VarScan.jar

ENV HTSLIB_INSTALL_DIR=/opt/htslib

WORKDIR /tmp
RUN wget https://github.com/samtools/htslib/releases/download/1.3.2/htslib-1.3.2.tar.bz2 && \
    tar --bzip2 -xvf htslib-1.3.2.tar.bz2 && \
    cd /tmp/htslib-1.3.2 && \
    ./configure  --enable-plugins --prefix=$HTSLIB_INSTALL_DIR && \
    make && \
    make install && \
    cp $HTSLIB_INSTALL_DIR/lib/libhts.so* /usr/lib/ && \
    ln -s $HTSLIB_INSTALL_DIR/bin/tabix /usr/bin/tabix

################
#Samtools 1.3.1#
################
ENV SAMTOOLS_INSTALL_DIR=/opt/samtools

WORKDIR /tmp
RUN wget https://github.com/samtools/samtools/releases/download/1.3.1/samtools-1.3.1.tar.bz2 && \
    tar --bzip2 -xf samtools-1.3.1.tar.bz2 && \
    cd /tmp/samtools-1.3.1 && \
    ./configure --with-htslib=$HTSLIB_INSTALL_DIR --prefix=$SAMTOOLS_INSTALL_DIR && \
    make && \
    make install && \
    ln -s /opt/samtools/bin/* /usr/local/bin/ && \
    cd / && \
    rm -rf /tmp/samtools-1.3.1
