FROM ubuntu:14.04

MAINTAINER Meng Bo "mengbo@lnu.edu.cn"

RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get -y install curl build-essential

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
  curl http://download.dnscrypt.org/dnscrypt-proxy/dnscrypt-proxy-1.4.0.tar.bz2 | tar xj;\
  cd dnscrypt-proxy*;\
  ./configure && make -j2;\
  make install

ADD run.sh /run.sh
RUN chmod +x /run.sh

EXPOSE 53
EXPOSE 53/udp

CMD ["/run.sh"]
