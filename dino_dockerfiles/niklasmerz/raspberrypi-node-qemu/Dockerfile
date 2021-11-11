FROM resin/raspberrypi-node
MAINTAINER NiklasMerz

ENV QEMU_EXECVE 1
COPY . /usr/bin

WORKDIR /usr/src/app
COPY cross-build-start ./
COPY cross-build-end ./
