FROM debian:wheezy

RUN sed -i "s%http://httpredir.debian.org%http://ftp.us.debian.org%g" /etc/apt/sources.list

# add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added
RUN groupadd -r redis && useradd -r -g redis redis

RUN apt-get update \
    && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*

# grab gosu for easy step-down from root
RUN gpg --keyserver pgp.mit.edu --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4
RUN curl -o /usr/local/bin/gosu -SL "https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-architecture)" \
    && curl -o /usr/local/bin/gosu.asc -SL "https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-architecture).asc" \
    && gpg --verify /usr/local/bin/gosu.asc \
    && rm /usr/local/bin/gosu.asc \
    && chmod +x /usr/local/bin/gosu

ENV REDIS_VERSION 2.4.18
ENV REDIS_DOWNLOAD_URL https://github.com/antirez/redis/archive/${REDIS_VERSION}.zip

RUN buildDeps='gcc libc6-dev make unzip'; \
    set -x \
    && rm -rf /var/lib/apt/lists/* && apt-get clean && apt-get update && apt-get install -y $buildDeps --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /usr/src/redis \
    && curl -sSL "$REDIS_DOWNLOAD_URL" -o redis.zip \
    && unzip redis.zip -d /usr/src/redis \
    && rm redis.zip \
    && make -C /usr/src/redis/redis-${REDIS_VERSION} \
    && make -C /usr/src/redis/redis-${REDIS_VERSION} install \
    && rm -r /usr/src/redis \
    && apt-get purge -y --auto-remove $buildDeps

RUN mkdir /data && chown redis:redis /data
VOLUME /data
WORKDIR /data

COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 6379
CMD [ "redis-server" ]
