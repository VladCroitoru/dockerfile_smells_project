FROM openjdk:8u141-jre
MAINTAINER magic@wizardtales.com

# Export HTTP & Transport
EXPOSE 9200 9300

ENV ES_VERSION 5.6.3

ENV DOWNLOAD_URL "https://artifacts.elastic.co/downloads/elasticsearch"
ENV ES_TARBAL "${DOWNLOAD_URL}/elasticsearch-${ES_VERSION}.tar.gz"
ENV ES_TARBALL_ASC "${DOWNLOAD_URL}/elasticsearch-${ES_VERSION}.tar.gz.asc"
ENV GPG_KEY "46095ACC8548582C1A2699A9D27D666CD88E42B4"

# Install Elasticsearch.
RUN apt-get update && apt-get install build-essential uuid-runtime -y && cd /tmp \
  && curl https://github.com/ncopa/su-exec/archive/v0.2.tar.gz -L | tar xz \
  && cd su-exec-0.2 && make && cp su-exec /usr/bin/ && cd .. \
  && echo "===> Install Elasticsearch..." \
  && curl -o elasticsearch.tar.gz -Lskj "$ES_TARBAL"; \
	if [ "$ES_TARBALL_ASC" ]; then \
		curl -o elasticsearch.tar.gz.asc -Lskj "$ES_TARBALL_ASC"; \
		export GNUPGHOME="$(mktemp -d)"; \
		gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEY"; \
		gpg --batch --verify elasticsearch.tar.gz.asc elasticsearch.tar.gz; \
		rm -r "$GNUPGHOME" elasticsearch.tar.gz.asc; \
	fi; \
  tar -xf elasticsearch.tar.gz \
  && ls -lah \
  && mv elasticsearch-$ES_VERSION /elasticsearch \
  && adduser --disabled-password --gecos "" --no-create-home --shell /sbin/nologin elasticsearch \
  && echo "===> Creating Elasticsearch Paths..." \
  && for path in \
  	/elasticsearch/config \
  	/elasticsearch/config/scripts \
  	/elasticsearch/plugins \
  ; do \
  mkdir -p "$path"; \
  chown -R elasticsearch:elasticsearch "$path"; \
  done \
  && rm -rf /tmp/* \
  && apt-get purge build-essential -y \
  && apt-get autoremove -y \
  && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV PATH /elasticsearch/bin:$PATH

WORKDIR /elasticsearch

# Copy configuration
COPY config /elasticsearch/config

# Copy run script
COPY run.sh /

# Set environment variables defaults
ENV ES_JAVA_OPTS "-Xms512m -Xmx512m"
ENV CLUSTER_NAME elasticsearch-default
ENV NODE_MASTER true
ENV NODE_DATA true
ENV NODE_INGEST true
ENV HTTP_ENABLE true
ENV NETWORK_HOST _site_
ENV HTTP_CORS_ENABLE true
ENV HTTP_CORS_ALLOW_ORIGIN *
ENV NUMBER_OF_MASTERS 1
ENV MAX_LOCAL_STORAGE_NODES 1
ENV SHARD_ALLOCATION_AWARENESS ""
ENV SHARD_ALLOCATION_AWARENESS_ATTR ""
ENV MEMORY_LOCK true

# Volume for Elasticsearch data
VOLUME ["/data"]

CMD ["/run.sh"]
