FROM ubuntu:14.04
MAINTAINER Greg Helton <greg@fallendusk.com>

RUN useradd -u 1000 mumble \
 && apt-get update \
 && apt-get install -y mumble-server \
 && mkdir /data && chown 1000 /data

ADD mumble-server.ini /config/mumble-server.ini

VOLUME ["/data", "/config"]
EXPOSE 64738/udp
EXPOSE 6502/tcp

USER mumble
ENTRYPOINT ["/usr/sbin/murmurd", "-fg", "-ini", "/config/mumble-server.ini"]
