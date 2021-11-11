FROM ubuntu:xenial
# enable all the sources
RUN sed -i 's/^#\s*\(deb.*\)$/\1/g' /etc/apt/sources.list && \
    sed -i 's/^#\s*\(deb-src.*\)$/\1/g' /etc/apt/sources.list
# update/upgrade
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get dist-upgrade -y && \
    apt-get install -y nano kpartx zerofree rsync build-essential wget apt-utils flex bison unzip && \
    apt-get build-dep -y qemu-system-arm && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /root/qemu
ADD https://download.qemu.org/qemu-2.10.1.tar.xz .
RUN tar xJf qemu-2.10.1.tar.xz --strip-components=1 --overwrite && \
    ./configure && \
    make -j`grep -c ^processor /proc/cpuinfo` && \
    make install && \
    qemu-system-arm --version && \
    qemu-system-arm --machine help
RUN rm -Rf /root/qemu
WORKDIR /root
ENTRYPOINT [ "bash" ]
