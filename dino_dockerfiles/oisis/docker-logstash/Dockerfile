FROM openjdk:8-jre

ENV GOSU_VERSION 1.7
ENV LOGSTASH_MAJOR 2.4
ENV LOGSTASH_VERSION 1:2.4.0-1
ENV PATH /opt/logstash/bin:$PATH
ENV LS_SETTINGS_DIR /etc/logstash
ENV LOGSTASH_PLUGINS logstash-codec-collectd logstash-output-elasticsearch

# install plugin dependencies
RUN apt-get update \
	&& apt-get install -y --no-install-recommends libzmq3 python-pip \
	&& pip install envtpl \
	&& rm -rf /var/lib/apt/lists/*

# the "ffi-rzmq-core" gem is very picky about where it looks for libzmq.so
RUN mkdir -p /usr/local/lib \
	&& ln -s /usr/lib/*/libzmq.so.3 /usr/local/lib/libzmq.so

# grab gosu for easy step-down from root
RUN set -x \
	&& wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture)" \
	&& wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture).asc" \
	&& export GNUPGHOME="$(mktemp -d)" \
	&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
	&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
	&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \
	&& chmod +x /usr/local/bin/gosu \
	&& gosu nobody true

RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys 46095ACC8548582C1A2699A9D27D666CD88E42B4

RUN echo "deb http://packages.elastic.co/logstash/${LOGSTASH_MAJOR}/debian stable main" > /etc/apt/sources.list.d/logstash.list

RUN set -x \
	&& apt-get update \
	&& apt-get install -y --no-install-recommends logstash=$LOGSTASH_VERSION \
	&& rm -rf /var/lib/apt/lists/*

# Install Logstash plugins
RUN /opt/logstash/bin/logstash-plugin install $LOGSTASH_PLUGINS

# comment out some troublesome configuration parameters
#   path.log: logs should go to stdout
#   path.config: No config files found: /etc/logstash/conf.d/*
RUN set -ex \
	&& if [ -f "$LS_SETTINGS_DIR/logstash.yml" ]; then \
		sed -ri 's!^(path.log|path.config):!#&!g' "$LS_SETTINGS_DIR/logstash.yml"; \
	fi

COPY config/logstash.conf.tpl /etc/logstash/conf.d/
COPY scripts/docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["-e", ""]
