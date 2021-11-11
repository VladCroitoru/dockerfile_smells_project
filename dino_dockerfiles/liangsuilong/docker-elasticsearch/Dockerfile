FROM liangsuilong/docker-java:8u151-b12

MAINTAINER Suilong Liang <suilong.liang@worktogether.io>

RUN groupadd -r elasticsearch && useradd -r -g elasticsearch elasticsearch

ENV ELASTICSEARCH_VERSION 6.2.1

ENV GOSU_VERSION 1.10
RUN set -x \
	&& apt-get update && apt-get install -y --no-install-recommends wget && rm -rf /var/lib/apt/lists/* \
	&& wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture)" \
	&& wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture).asc" \
	&& export GNUPGHOME="$(mktemp -d)" \
	&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
	&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
	&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \
	&& chmod +x /usr/local/bin/gosu \
	&& gosu nobody true \
	&& apt-get purge -y wget

RUN set -x \
	&& apt-get update && apt-get install -y --no-install-recommends  wget && rm -rf /var/lib/apt/lists/* \
	&& wget -O /opt/elasticsearch.tar.gz "https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-${ELASTICSEARCH_VERSION}.tar.gz" \
	&& cd /opt/ \
	&& tar xvf elasticsearch.tar.gz \
	&& mv elasticsearch-${ELASTICSEARCH_VERSION} elasticsearch \
	&& rm -f elasticsearch.tar.gz \
	&& chown -R elasticsearch:elasticsearch /opt/elasticsearch/ \
	&& apt-get purge -y wget

ADD entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

VOLUME ["/opt/elasticsearch/data/", "/etc/elasticsearch/", "/opt/elasticsearch/logs/", "/opt/elasticsearch/plugins/"]
EXPOSE 9200 9300

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["elasticsearch"]
