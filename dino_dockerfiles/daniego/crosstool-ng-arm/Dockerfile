FROM ubuntu:xenial
MAINTAINER Daniel Floris <daniel.floris@gmail.com>

RUN apt-get update && \
    apt-get install -y \
		autoconf \
		automake \
		binutils \
		bison \
		build-essential \
		curl \
		flex \
		gawk \
		gperf \
		libncurses5-dev \
		libtool \
    libtool-bin \
    help2man \
		subversion \
		texinfo \
		tmux \
		unzip \
		wget

ENV CROSSTOOL_NG_VERSION 1.23.0
RUN echo $CROSSTOOl_NG_VERSION
RUN curl -s http://crosstool-ng.org/download/crosstool-ng/crosstool-ng-${CROSSTOOL_NG_VERSION}.tar.bz2 | tar -jx -C /usr/src
WORKDIR /usr/src/crosstool-ng-${CROSSTOOL_NG_VERSION}
RUN ./configure --prefix=/opt/cross && \
    make && \
    make install

ADD ct-ng-config /root/ct-ng-conf/.config
ADD ct-ng-env /usr/local/bin/ct-ng-env
RUN chmod +x /usr/local/bin/ct-ng-env

RUN apt-get remove -y wget unzip curl subversion && \
		apt-get autoremove -y && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /
