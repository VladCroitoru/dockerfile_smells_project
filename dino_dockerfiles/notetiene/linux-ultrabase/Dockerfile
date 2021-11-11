ARG VERSION=latest
FROM notetiene/linux-base:$VERSION

MAINTAINER Etienne Prud’homme <e.e.f.prudhomme@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN echo 'APT::Get::Assume-Yes "true";' >> /etc/apt/apt.conf \
    && apt-get update && apt-get upgrade

# Build tools
RUN apt-get install \
    autoconf \
    automake \
    autotools-dev \
    libtool \
    libtool-bin \
    cmake \
    cmake-curses-gui \
    ninja-build

# Archive & compression support
RUN apt-get install \
    p7zip-full \
    p7zip-rar \
    valgrind

# Documentation
RUN apt-get install \
    texinfo \
    texinfo-doc-nonfree \
    info \
    man \
    manpages

# Language
RUN apt-get install \
    ispell \
    aspell \
    hunspell

# Version control system
RUN apt-get install \
    git \
    bzr \
    cvs \
    subversion

# Terminal Utilities
RUN apt-get install \
    htop \
    multitail \
    tree \
    gnupg2 \
    gpm

# For compiler development
RUN apt-get install \
    flex \
    bison

# Support for PPAs
RUN apt-get install \
    software-properties-common

RUN tac /etc/apt/apt.conf \
    | sed '0,/APT::Get::Assume-Yes "true";/{/APT::Get::Assume-Yes "true";/d;}' \
    | tac > /etc/apt/apt.conf
