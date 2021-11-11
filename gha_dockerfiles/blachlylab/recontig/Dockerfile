FROM ubuntu:20.04

LABEL description="Docker image for recontig with PyD"

ARG DEBIAN_FRONTEND=noninteractive
# Change htslib version here
ENV HTSLIB_VERSION 1.13  
ENV PACKAGES autoconf automake make gcc perl pip git \
    curl zlib1g-dev libbz2-dev liblzma-dev libssl-dev \
    libcurl4-gnutls-dev libxml2

ENV RECONTIG_VERSION 1.2.0

ENV LD_LIBRARY_PATH /usr/local/lib
ENV LIBRARY_PATH /usr/local/lib

# Install htslib Dependencies and library
# Install packages
RUN apt-get update && apt-get install \
    && apt-get install -y ${PACKAGES} && apt-get clean

ADD https://github.com/samtools/htslib/releases/download/${HTSLIB_VERSION}/htslib-${HTSLIB_VERSION}.tar.bz2 /usr/local/

WORKDIR /usr/local/ 

RUN tar -xvf /usr/local/htslib-${HTSLIB_VERSION}.tar.bz2

WORKDIR /usr/local/htslib-${HTSLIB_VERSION}

RUN ./configure 

RUN make install

WORKDIR /usr/local/

# Install the ldc
RUN curl https://dlang.org/install.sh | bash -s ldc

# Install CPython and pyd
RUN pip install cython pyd

# Install recontig

RUN git clone --recurse-submodules https://github.com/blachlylab/recontig.git

WORKDIR /usr/local/recontig

RUN git checkout v${RECONTIG_VERSION}

RUN . ~/dlang/ldc-*/activate && dub build

RUN mv recontig /usr/local/bin

# Define default location
ENTRYPOINT ["recontig"]
