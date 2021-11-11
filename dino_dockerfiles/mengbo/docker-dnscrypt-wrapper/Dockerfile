FROM ubuntu:14.04

MAINTAINER Meng Bo "mengbo@lnu.edu.cn"

RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get -y install curl git autoconf automake build-essential libevent-dev

RUN mkdir -p /usr/local/src;\
  cd /usr/local/src;\
  curl https://download.libsodium.org/libsodium/releases/libsodium-0.5.0.tar.gz | tar xz;\
  cd libsodium*;\
  ./configure;\
  make && make check;\
  make install

RUN echo /usr/local/lib > /etc/ld.so.conf.d/usr_local_lib.conf;\
  ldconfig;

RUN mkdir -p /usr/local/src;\
  cd /usr/local/src;\
  git clone --progress --recursive git://github.com/Cofyc/dnscrypt-wrapper.git;\
  cd dnscrypt-wrapper;\
  make configure;\
  ./configure;\
  make install

ADD run.sh /run.sh
RUN chmod +x /run.sh

VOLUME ["/usr/local/share/dnscrypt-wrapper"]

EXPOSE 443
EXPOSE 443/udp

CMD ["/run.sh"]
