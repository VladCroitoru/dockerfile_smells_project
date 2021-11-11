FROM qnib/dplain-openjdk8


# ensure elasticsearch user exists
RUN groupadd elasticsearch \
 && useradd -g elasticsearch elasticsearch


RUN set -ex; \
# https://artifacts.elastic.co/GPG-KEY-elasticsearch
	key='46095ACC8548582C1A2699A9D27D666CD88E42B4'; \
	export GNUPGHOME="$(mktemp -d)"; \
	gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
	gpg --export "$key" > /etc/apt/trusted.gpg.d/elastic.gpg; \
	rm -r "$GNUPGHOME"; \
	apt-key list

# https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-repositories.html
# https://www.elastic.co/guide/en/elasticsearch/reference/5.0/deb.html
RUN set -x \
 && apt-get update \
 && apt-get install -y curl nmap jq vim sed \
 && apt-get install -y --no-install-recommends apt-transport-https && rm -rf /var/lib/apt/lists/* \
 && echo 'deb https://artifacts.elastic.co/packages/6.x/apt stable main' > /etc/apt/sources.list.d/elasticsearch.list

ARG ELASTICSEARCH_VERSION=6.3.2
ARG ELASTICSEARCH_DEB_VERSION=6.3.2
ENV ES_JAVA_OPTS="-Dlog4j2.disable.jmx=true"

RUN set -x \
	\
# don't allow the package to install its sysctl file (causes the install to fail)
# Failed to write '262144' to '/proc/sys/vm/max_map_count': Read-only file system
	&& dpkg-divert --rename /usr/lib/sysctl.d/elasticsearch.conf \
	\
	&& apt-get update \
	&& apt-get install -y --no-install-recommends "elasticsearch=$ELASTICSEARCH_DEB_VERSION" \
	&& rm -rf /var/lib/apt/lists/*

ENV PATH /usr/share/elasticsearch/bin:$PATH

WORKDIR /etc/elasticsearch

RUN set -ex \
	&& for path in \
		./data \
		./logs \
		./config \
		./config/scripts \
	; do \
		mkdir -p "$path"; \
		chown -R elasticsearch:elasticsearch "$path"; \
	done

WORKDIR /
RUN apt-get update \
 && apt-get install -y wget \
 && wget -qO /usr/local/bin/go-elastic-health https://github.com/qnib/go-elastic-health/releases/download/v1.0.0/go-elastic-health_Linux \
 && chmod +x /usr/local/bin/go-elastic-health \
 && apt-get purge -y wget \
 && rm -rf /var/lib/apt/lists/*
RUN elasticsearch-plugin install -b repository-s3
ENV ES_DATA=true \
    ES_MASTER=true \
    ES_NET_HOST=0.0.0.0 \
    ES_MLOCKAciLL=true \
    ES_HEAP_MAX=256m \
    ES_HEAP_MIN=256m \
    ENTRY_USER=elasticsearch
COPY opt/qnib/elasticsearch/index-registration/settings/*.json /opt/qnib/elasticsearch/index-registration/settings/
CMD ["elasticsearch"]
VOLUME ["/var/lib/elasticsearch", "/var/log/elasticsearch"]
COPY opt/entry/* /opt/entry/
COPY opt/healthchecks/*.sh /opt/healthchecks/
COPY opt/qnib/elasticsearch/etc/elasticsearch.yml \
     opt/qnib/elasticsearch/etc/log4j2.properties \
     /etc/elasticsearch/
RUN echo "gosu elasticsearch elasticsearch" >> /root/.bash_history
