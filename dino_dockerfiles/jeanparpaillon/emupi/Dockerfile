FROM debian:jessie
MAINTAINER Jean Parpaillon <jean.parpaillon@free.fr>

ENV DEBIAN_FRONTEND noninteractive

RUN ( echo "deb http://cdn.debian.net/debian jessie main contrib non-free"; \
      echo "deb-src http://cdn.debian.net/debian jessie main contrib non-free"; \
      echo "deb http://cdn.debian.net/debian jessie-updates main contrib non-free"; \
      echo "deb-src http://cdn.debian.net/debian jessie-updates main contrib non-free"; \
      echo "deb http://security.debian.org jessie/updates main contrib non-free"; \
      echo "deb-src http://security.debian.org jessie/updates main contrib non-free" ) \
      > /etc/apt/sources.list && \
    apt-get update && \
    apt-get -y install wget apt-utils build-essential git devscripts ca-certificates zip debhelper pkg-config x11-apps libfdt-dev &&  \
    apt-get clean
RUN git clone --depth 1 --branch rpi https://github.com/Torlus/qemu.git
RUN cd qemu && git checkout `cat /root/qemu.lock`
RUN apt-get update && apt-get -y build-dep qemu && apt-get clean
RUN cd qemu && ./configure --prefix=/opt/qemu-rpi --target-list=arm-softmmu && make && make install
RUN for i in `seq 0 7`; do mknod /dev/loop$i b -m0660 7 $i; done

ADD emupi /root/emupi
ADD rpimount /root/rpimount
ADD blkoffset /root/blkoffset
ADD qemu.lock /root/qemu.lock

ENTRYPOINT ["/root/emupi", "/rpi.img"]
