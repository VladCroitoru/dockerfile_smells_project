FROM ubuntu:16.04
LABEL maintainer="Thomas Kärgel kaergel at b1-systems.de"
ENV REFRESHED_AT=20170408 LC_ALL=C.UTF-8 LANG=C.UTF-8
RUN useradd -m -s /bin/bash vds
RUN apt-get update; \
    apt-get upgrade -y; \
    apt-get install -y libxml2 libxslt1.1 zlib1g python3-pip; \
    pip3 install -U pip; \
    pip3 install vdirsyncer
USER vds
RUN mkdir -p /home/vds/.config/vdirsyncer/
COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
