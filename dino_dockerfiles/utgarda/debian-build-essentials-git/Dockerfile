FROM debian:jessie
MAINTAINER Aleksandr Mezin <mezin.alexander@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
RUN echo "deb http://httpredir.debian.org/debian jessie contrib non-free" > /etc/apt/sources.list.d/nonfree.list && \
    echo "deb http://httpredir.debian.org/debian jessie-updates contrib non-free" >> /etc/apt/sources.list.d/nonfree.list && \
    echo "deb http://security.debian.org jessie/updates contrib non-free" >> /etc/apt/sources.list.d/nonfree.list && \
    apt-get update && \
    apt-get -y install devscripts build-essential debhelper git cmake bison flex libssl-dev libpcap-dev
