#
# Dockerfile to build an image with Virtuoso Universal Server.
#

FROM ubuntu:16.04

MAINTAINER Arnold Kuzniar <a.kuzniar@esciencecenter.nl>

# update packages & install dependencies for Virtuoso
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    automake \
    gperf \
    gawk \
    libtool \
    flex \
    bison \
    libssl-dev \
    net-tools \
    vim \
    curl \
    && rm -rf /var/lib/apt/lists/*

# set command-line args including defaults
ARG VOS_VERSION=stable/7
ARG VOS_PREFIX=/usr/local/virtuoso-opensource
ARG VOS_MAXROWS=100000
ARG VOS_MAXVECSZ=3000000
ARG VOS_ADJVECSZ=1
ARG VOS_NUMBUF=340000
ARG VOS_MAXDRTBUF=250000

# compile & install Virtuoso including serveral VAD packages
WORKDIR /tmp
RUN git clone -b ${VOS_VERSION} https://github.com/openlink/virtuoso-opensource.git
WORKDIR virtuoso-opensource
ENV CFLAGS="-O2 -m64"
RUN ./autogen.sh && ./configure --prefix=${VOS_PREFIX} \
    --enable-conductor-vad \
    --enable-rdb2rdf-vad \
    --enable-rdfmappers-vad \
    --enable-fct-vad \
    && make -j $(nproc) && make install
WORKDIR /tmp
RUN rm -fr virtuoso-opensource

# add Virtuoso binaries to PATH
ENV PATH=${VOS_PREFIX}/bin:${PATH}

# add volume for file sharing
ENV VOS_SHARE=/tmp/share
VOLUME ${VOS_SHARE}

# modify Virtuoso config file
ENV VOS_CONFIG=${VOS_PREFIX}/var/lib/virtuoso/db/virtuoso.ini
RUN sed -i "/DirsAllowed/ s:$:,${VOS_SHARE}:" ${VOS_CONFIG}
RUN sed -i "/ResultSetMaxRows/ s:=\s*[0-9]*:= ${VOS_MAXROWS}:" ${VOS_CONFIG}
RUN sed -i "/MaxVectorSize/ s:=\s*[0-9]*:= ${VOS_MAXVECSZ}:" ${VOS_CONFIG}
RUN sed -i "/AdjustVectorSize/ s:=\s*[0-9]*:= ${VOS_ADJVECSZ}:" ${VOS_CONFIG}
RUN sed -i "/^NumberOfBuffers/ s:=\s*[0-9]*:= ${VOS_NUMBUF}:" ${VOS_CONFIG}
RUN sed -i "/^MaxDirtyBuffers/ s:=\s*[0-9]*:= ${VOS_MAXDRTBUF}:" ${VOS_CONFIG}
WORKDIR ${VOS_SHARE}

# expose (default) Virtuoso server ports
EXPOSE 8890
EXPOSE 1111

# start Virtuoso server
CMD ["sh", "-c", "virtuoso-t +wait +foreground +configfile ${VOS_CONFIG}"]
