FROM ubuntu:15.04

MAINTAINER Justin Cormack <justin@specialbusservice.com>

RUN apt-get update && apt-get install -y \
  binutils \
  cpp \
  curl \
  g++ \
  gcc \
  git \
  libc6-dev \
  strace \
  gawk \
  libxen-dev \
  xen-utils-common \
  xen-utils-4.5 \
  qemu-system-x86 \
  gcc-multilib \
  vim \
  file \
  genisoimage \
  bzip2 \
  xz-utils \
  python3.4 \
  libssl-dev \
  bison \
  autoconf \
  automake \
  cmake \
  makefs \
  make

COPY . /usr/src/rumprun-hw
RUN cd /usr/src/rumprun-hw && git submodule update --init && \
  cd /usr/src && cp -a rumprun-hw rumprun-xen

#ENV PATH=$PATH:/usr/src/rumprun/app-tools

WORKDIR /usr/src/rumprun-hw

RUN ./build-rr.sh hw
#RUN \
#  ./tests/buildtests.sh x86_64 hw elf && \
#  ./tests/runtests.sh qemu

WORKDIR /usr/src/rumprun-xen

RUN ./build-rr.sh xen
