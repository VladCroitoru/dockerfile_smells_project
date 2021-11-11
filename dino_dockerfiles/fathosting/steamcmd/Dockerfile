FROM debian:jessie-slim
MAINTAINER FAT <contact@fat.sh>

ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

ENV GOSU_VERSION 1.10
RUN set -x \
    && apt-get update && apt-get install -y --no-install-recommends ca-certificates wget && rm -rf /var/lib/apt/lists/* \
    && dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \
    && wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch" \
    && wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc" \
    && export GNUPGHOME="$(mktemp -d)" \
    && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
    && gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
    && rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \
    && chmod +x /usr/local/bin/gosu \
    && gosu nobody true \
    && apt-get purge -y --auto-remove ca-certificates wget

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    lib32gcc1 \
    lib32ncurses5 \
    lsyncd \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd -r steam && useradd -r -d /home/steam -g steam steam

WORKDIR /home/steam

RUN curl -sqL "https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz" | tar zxvf -

RUN mkdir .steam \
    && ln -s /home/steam/linux32 .steam/sdk32 \
    && ln -s /home/steam/linux64 .steam/sdk64

RUN chown -R steam:steam /home/steam

RUN gosu steam bash -c "./steamcmd.sh +login anonymous +quit"
