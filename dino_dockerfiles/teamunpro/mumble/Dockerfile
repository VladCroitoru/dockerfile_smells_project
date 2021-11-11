FROM ubuntu:14.04
MAINTAINER Mark McGuire <mark.b.mcg@gmail.com>

RUN useradd -u 1000 mumble \
 && apt-get update \
 && apt-get install -y mumble-server awscli curl \
 && mkdir /data && chown 1000 /data

ADD mumble-server.ini /config/mumble-server.ini
ADD start.sh /start.sh

VOLUME ["/data", "/config"]
EXPOSE 64738/udp

USER mumble
ENTRYPOINT ["/bin/sh", "/start.sh"]
