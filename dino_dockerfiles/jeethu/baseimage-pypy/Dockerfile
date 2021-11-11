FROM phusion/baseimage:0.9.21
MAINTAINER Jeethu Rao <jeethu.rao@dubizzle.com>

ENV LANG=C.UTF-8 DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install bzip2 \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY scripts/ /root/scripts/

RUN /bin/bash /root/scripts/install_pypy.sh
