FROM ubuntu:16.04

MAINTAINER Suilong Liang <suilong.liang@worktogether.io>

# add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added
RUN groupadd -r redis && useradd -r -g redis redis

# grab gosu for easy step-down from root
# https://github.com/tianon/gosu/releases

ENV REDIS_VERSION 4.0.6
ENV REDIS_VERSION_MINOR 1chl1~xenial1
ENV GOSU_VERSION 1.10
RUN set -ex; \
	\
	fetchDeps='ca-certificates wget'; \
	apt-get update; \
	apt-get install -y --no-install-recommends $fetchDeps; \
	rm -rf /var/lib/apt/lists/*; \
	\
	dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')"; \
	wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"; \
	wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"; \
	export GNUPGHOME="$(mktemp -d)"; \
	gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4; \
	gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu; \
	rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc; \
	chmod +x /usr/local/bin/gosu; \
	gosu nobody true; \
	\
	apt-get purge -y --auto-remove $fetchDeps

# Manually Add Redis PPA https://launchpad.net/~chris-lea/+archive/ubuntu/redis-server
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 136221EE520DDFAF0A905689B9316A7BC7917B12

RUN echo "deb http://ppa.launchpad.net/chris-lea/redis-server/ubuntu xenial main" > /etc/apt/sources.list.d/redis.list && \
    apt-get -y update && \
    apt-get -y install redis-server=4:${REDIS_VERSION}-${REDIS_VERSION_MINOR} \
	redis-sentinel=4:${REDIS_VERSION}-${REDIS_VERSION_MINOR} \
	redis-tools=4:${REDIS_VERSION}-${REDIS_VERSION_MINOR} && \
    rm -rf /var/lib/apt/list/*

RUN mkdir -p /etc/redis/conf.d/

VOLUME /var/lib/redis/ /etc/redis/conf.d/ /var/log/redis/

ADD entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

EXPOSE 6379
CMD ["start"]
