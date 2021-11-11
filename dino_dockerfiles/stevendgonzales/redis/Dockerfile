FROM ubuntu:trusty

RUN apt-get update && apt-get install -y --no-install-recommends curl \
	&& rm -rf /var/lib/apt/lists/*

ENV REDIS_VERSION 3.0.3
ENV REDIS_DOWNLOAD_URL http://download.redis.io/releases/redis-3.0.3.tar.gz
ENV REDIS_DOWNLOAD_SHA1 0e2d7707327986ae652df717059354b358b83358

RUN buildDeps='gcc libc6-dev make' \
	&& set -x \
	&& apt-get update && apt-get install -y $buildDeps --no-install-recommends \
	&& rm -rf /var/lib/apt/lists/* \
	&& mkdir -p /usr/src/redis \
	&& curl -sSL "$REDIS_DOWNLOAD_URL" -o redis.tar.gz \
	&& echo "$REDIS_DOWNLOAD_SHA1 *redis.tar.gz" | sha1sum -c - \
	&& tar -xzf redis.tar.gz -C /usr/src/redis --strip-components=1 \
	&& rm redis.tar.gz \
	&& make -C /usr/src/redis \
	&& make -C /usr/src/redis install \
	&& rm -r /usr/src/redis \
	&& apt-get purge -y --auto-remove $buildDeps

RUN mkdir /etc/redis/ \
    && mkdir /var/log/redis \
    && mkdir /data

COPY redis.conf /etc/redis/redis.conf

VOLUME /data
WORKDIR /data

EXPOSE 6379
CMD [ "redis-server", "/etc/redis/redis.conf" ]
