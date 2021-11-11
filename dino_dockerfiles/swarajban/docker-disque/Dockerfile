FROM debian:jessie
MAINTAINER Swaraj Banerjee <swarajban@gmail.com>

# add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added
RUN groupadd -r disque && useradd -r -g disque disque

RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
    && rm -rf /var/lib/apt/lists/*

# grab gosu for easy step-down from root
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4
RUN curl -o /usr/local/bin/gosu -fSL "https://github.com/tianon/gosu/releases/download/1.7/gosu-$(dpkg --print-architecture)" \
    && curl -o /usr/local/bin/gosu.asc -fSL "https://github.com/tianon/gosu/releases/download/1.7/gosu-$(dpkg --print-architecture).asc" \
    && gpg --verify /usr/local/bin/gosu.asc \
    && rm /usr/local/bin/gosu.asc \
    && chmod +x /usr/local/bin/gosu

ENV DISQUE_VERSION 1.0-rc1
ENV DISQUE_DOWNLOAD_URL https://github.com/antirez/disque/archive/1.0-rc1.tar.gz
ENV DISQUE_DOWNLOAD_SHA1 b82a588a12994a14d5a2817b485be2f21808ad6a

RUN buildDeps='gcc libc6-dev make' \
    && set -x \
    && apt-get update && apt-get install -y $buildDeps --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /usr/src/disque \
    && curl -sSL "$DISQUE_DOWNLOAD_URL" -o disque.tar.gz \
    && echo "$DISQUE_DOWNLOAD_SHA1 *disque.tar.gz" | sha1sum -c - \
    && tar -xzf disque.tar.gz -C /usr/src/disque --strip-components=1 \
    && rm disque.tar.gz \
    && make -C /usr/src/disque \
    && make -C /usr/src/disque install \
    && rm -r /usr/src/disque \
    && apt-get purge -y --auto-remove $buildDeps

RUN mkdir /data && chown disque:disque /data
VOLUME /data
WORKDIR /data

COPY docker-entrypoint.sh /entrypoint.sh
COPY disque.conf /usr/local/etc/disque/disque.conf
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 7711 17711
CMD [ "disque-server", "/usr/local/etc/disque/disque.conf" ]
