FROM debian:stretch
MAINTAINER cutech <cody@c-u-tech.com>

RUN useradd -u 1000 mumble \
 && apt-get update \
 && apt-get install -y mumble-server wget unzip screen nano procps \
 && mkdir -p /murmur/data /murmur/config
 
ADD mumble-server.ini /murmur/config/mumble-server.ini
ADD mumble-server.ini /murmur/config/murmur.ini
ADD gtmurmur-static /murmur/config

RUN chmod +x /murmur/config/gtmurmur-static && chown -R 1000:1000 /murmur

VOLUME ["/murmur"]

EXPOSE 64738
EXPOSE 64738/udp
EXPOSE 27800
EXPOSE 27800/udp

USER mumble

ENTRYPOINT ["/usr/sbin/murmurd", "-fg", "-ini", "/murmur/config/mumble-server.ini"]
