FROM ubuntu:16.04

MAINTAINER Skepickle

RUN DEBIAN_FRONTEND=noninteractive set -x \
    && apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends \
         ca-certificates wget \
         libterm-readkey-perl libterm-readline-gnu-perl \
    && rm -rf /var/lib/apt/lists/*

ENV GOSU_VERSION 1.9
RUN set -x \
    && wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture)" \
    && wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture).asc" \
    && export GNUPGHOME="$(mktemp -d)" \
    && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
    && gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
    && rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \
    && chmod +x /usr/local/bin/gosu \
    && gosu nobody true

RUN mkdir /mc_data
VOLUME /mc_data

COPY src/* /tmp/
RUN chmod +x /tmp/entrypoint.sh
RUN chmod +x /tmp/wrapper.pl

EXPOSE 25565/tcp
EXPOSE 25565/udp
EXPOSE 25575/tcp

ENTRYPOINT ["/tmp/entrypoint.sh"]

