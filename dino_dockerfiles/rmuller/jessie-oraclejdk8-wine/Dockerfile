# Dockerfile for 'rmuller/jessie-oraclejdk8-wine'
#
FROM rmuller/jessie-oraclejdk8:1.0.0
MAINTAINER Ronald K. Muller <rmuller@xiam.nl>
WORKDIR /root/
ENV WINEARCH win32
RUN export DEBIAN_FRONTEND=noninteractive &&\
    echo 'deb http://deb.debian.org/debian jessie-backports main' >> /etc/apt/sources.list &&\
    dpkg --add-architecture i386 &&\
    apt-get update -qq &&\
    apt-get install -qq lib32z1 lib32ncurses5 libbz2-1.0:i386 &&\
    apt-get -t jessie-backports install -qq wine32 &&\
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/* /var/log/apt/*
CMD /bin/bash
