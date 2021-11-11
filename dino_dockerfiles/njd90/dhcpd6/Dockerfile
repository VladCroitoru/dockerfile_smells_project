FROM ubuntu:xenial

MAINTAINER NJD <contact@skyblack.fr>

ARG DEBIAN_FRONTEND=noninteractive

LABEL Description="ISC DHCP server v6" \
        tags="" \
        maintainer="NJD <https://github.com/njd90>" \
        build_ver="201803031030"

RUN apt-get -q -y update \
 && apt-get -q -y -o "DPkg::Options::=--force-confold" -o "DPkg::Options::=--force-confdef" install apt-utils \
 && apt-get -q -y -o "DPkg::Options::=--force-confold" -o "DPkg::Options::=--force-confdef" dist-upgrade \
 && apt-get -q -y -o "DPkg::Options::=--force-confold" -o "DPkg::Options::=--force-confdef" install isc-dhcp-server man \
 && apt-get -q -y autoremove \
 && apt-get -q -y clean \
 && rm -rf /var/lib/apt/lists/*

COPY util/dumb-init_1.2.0_amd64 /usr/bin/dumb-init
COPY util/entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
