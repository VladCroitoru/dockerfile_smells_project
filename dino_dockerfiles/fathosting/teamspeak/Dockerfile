FROM debian:jessie
MAINTAINER FAT <contact@fat.sh>

ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN groupadd -r teamspeak && useradd -m -r -g teamspeak teamspeak

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
    curl \
    bzip2 \
    lsyncd \
    && rm -rf /var/lib/apt/lists/*

COPY lsyncd.conf.lua /etc/lsyncd/
COPY docker-entrypoint.sh /usr/local/bin/

ENV TS3_VERSION 3.0.13.7
RUN curl -s http://dl.4players.de/ts/releases/${TS3_VERSION}/teamspeak3-server_linux_amd64-${TS3_VERSION}.tar.bz2 | tar -jx -C /home/teamspeak

VOLUME ["/home/teamspeak/backup"]
EXPOSE 9987/udp 10011 30033

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["./ts3server"]
