FROM ubuntu:14.04
MAINTAINER Itsuugo <itsuugo@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y \
    build-essential \
    git-core \
    unzip \
    nasm \
    libssl-dev \
    libpcap-dev \
    subversion \
    curl \
    imagemagick\
    parallel \
    autoconf \
    libtool &&\
    apt-get -y build-dep qemu

RUN mkdir /src 
RUN cd /src ; git clone https://github.com/moyix/panda.git

# Install LVM
RUN cd /src/panda; svn checkout http://llvm.org/svn/llvm-project/llvm/tags/RELEASE_33/final/ llvm
RUN cd /src/panda/llvm/tools ; svn checkout http://llvm.org/svn/llvm-project/cfe/tags/RELEASE_33/final/ clang
RUN cd /src/panda/llvm/tools/clang/tools ; svn checkout http://llvm.org/svn/llvm-project/clang-tools-extra/tags/RELEASE_33/final/ extra
RUN cd /src/panda/llvm ; ./configure --enable-optimized --disable-assertions --enable-targets=x86 && REQUIRES_RTTI=1 make -j $(nproc)

# Install Distorm
RUN cd /src/panda ; svn checkout http://distorm.googlecode.com/svn/trunk/ distorm
RUN cd /src/panda/distorm/make/linux ; make && make install
RUN cd /src/panda/distorm/include ; cp * /usr/local/include

# Install Protocol buffers C style
RUN mkdir /src/software
RUN cd /src/software ; git clone https://github.com/google/protobuf.git
RUN cd /src/software/protobuf ; sh ./autogen.sh && ./configure --disable-shared && make && make install
RUN cd /src/software ; git clone https://github.com/protobuf-c/protobuf-c.git
RUN cd /src/software/protobuf-c ; sh ./autogen.sh && ./configure --disable-shared && make && make install

# Install Pycparser
RUN cd /src/software ; git clone https://github.com/eliben/pycparser.git
RUN cd /src/software/pycparser ; python setup.py install

# Install qemu Ubuntu 14.04 uses gcc 4.8
RUN cd /src/panda/qemu ; CC=gcc-4.8 CXX=g++-4.8 ./build.sh



