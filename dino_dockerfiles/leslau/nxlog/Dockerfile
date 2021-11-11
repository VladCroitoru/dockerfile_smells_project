FROM ubuntu:14.04

ENV NXLOG_VERSION=2.9.1716

MAINTAINER Luciano Mores <luciano.mores@gmail.com>

ADD https://nxlog.co/system/files/products/files/1/nxlog-ce_${NXLOG_VERSION}_ubuntu_1404_amd64.deb /data/

RUN apt-get update && \
    apt-get install -y libapr1 libdbi1 libperl5.18 openssl

RUN dpkg -i /data/nxlog-ce_${NXLOG_VERSION}_ubuntu_1404_amd64.deb
RUN apt-get autoremove -y -q

EXPOSE 514/tcp 514/udp

ENTRYPOINT ["/usr/bin/nxlog"]
CMD ["-f"]
