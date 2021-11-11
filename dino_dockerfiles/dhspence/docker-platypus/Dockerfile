FROM ubuntu:xenial
MAINTAINER David H. Spencer <dspencer@wustl.edu>

LABEL \
  description="Platypus image"

RUN apt-get update -y && apt-get install -y \
    wget \
    git \
    unzip \
    bzip2 \
    tar \
    g++ \
    gcc \
    zlib1g-dev \
    make \
    python \
    python-dev

##############
#HTSlib 1.3.2#
##############
ENV HTSLIB_INSTALL_DIR=/opt/htslib

WORKDIR /tmp
RUN wget https://github.com/samtools/htslib/releases/download/1.3.2/htslib-1.3.2.tar.bz2 && \
    tar --bzip2 -xvf htslib-1.3.2.tar.bz2

WORKDIR /tmp/htslib-1.3.2
RUN ./configure  --enable-plugins --prefix=$HTSLIB_INSTALL_DIR && \
    make && \
    make install && \
    cp $HTSLIB_INSTALL_DIR/lib/libhts.so* /usr/lib/


###############
#Platypus
###############

ENV PLATYPUS_DIR=/opt/platypus
RUN mkdir /opt/platypus

WORKDIR /opt/platypus
RUN wget http://www.well.ox.ac.uk/bioinformatics/Software/Platypus-latest.tgz && \
    tar -zxvf Platypus-latest.tgz

WORKDIR /opt/platypus/Platypus_0.8.1
RUN cp -r /tmp/htslib-1.3.2/htslib ./ && \
    ./buildPlatypus.sh

WORKDIR /
RUN rm -Rf /tmp/htslib*

ENTRYPOINT ["python", "/opt/platypus/Platypus_0.8.1/Platypus.py"]
