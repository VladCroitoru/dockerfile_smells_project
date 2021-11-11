# Rockchip development environment based on Ubuntu 17.04 LTS.
# version 0.0.1

# Start with Ubuntu 17.04 LTS.
#FROM debian:stretch
FROM ubuntu:17.04

MAINTAINER Terry Chan <terrygarbie@yahoo.com.hk>

ENV DEBIAN_FRONTEND=noninteractive

# First, install add-apt-repository and bzip2
RUN apt-get update && apt-get install -y \
    git-core \
    gitk \
    git-gui \
    make \
    gcc \
    g++ \
    wget \
    python \
    unzip \
    bc \
    automake \
    libncurses-dev \
    cpio \
    bzip2 \
    bison \
    flex \
    texinfo \
    \
    bc \
    binutils \
    build-essential \
    git \
    gzip \
    locales \
    libncurses5-dev \
    mercurial \
    whois \
    patch \
    perl \
    rsync \
    sed \
    tar \
    wget    

# Sometimes Buildroot need proper locale, e.g. when using a toolchain
# based on glibc.
RUN locale-gen en_US.utf8

	