FROM qnib/dplain-init


RUN groupadd -r kibana && useradd -r -m -g kibana kibana

RUN apt-get update && apt-get install -y \
		apt-transport-https \
		ca-certificates \
		wget \
# generating PDFs requires libfontconfig and libfreetype6
		libfontconfig \
		libfreetype6 \
	--no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN set -ex; \
# https://artifacts.elastic.co/GPG-KEY-elasticsearch
	key='46095ACC8548582C1A2699A9D27D666CD88E42B4'; \
	export GNUPGHOME="$(mktemp -d)"; \
	gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
	gpg --export "$key" > /etc/apt/trusted.gpg.d/elastic.gpg; \
	rm -r "$GNUPGHOME"; \
	apt-key list

# https://www.elastic.co/guide/en/kibana/5.0/deb.html
RUN echo 'deb https://artifacts.elastic.co/packages/5.x/apt stable main' > /etc/apt/sources.list.d/kibana.list

ENV KIBANA_VERSION 5.5.1

RUN set -x \
	&& apt-get update \
	&& apt-get install -y --no-install-recommends kibana=$KIBANA_VERSION \
	&& rm -rf /var/lib/apt/lists/* \
	\
# the default "server.host" is "localhost" in 5+
	&& sed -ri "s!^(\#\s*)?(server\.host:).*!\2 '0.0.0.0'!" /etc/kibana/kibana.yml \
	&& grep -q "^server\.host: '0.0.0.0'\$" /etc/kibana/kibana.yml \
	\
# ensure the default configuration is useful when using --link
	&& sed -ri "s!^(\#\s*)?(elasticsearch\.url:).*!\2 'http://elasticsearch:9200'!" /etc/kibana/kibana.yml \
	&& grep -q "^elasticsearch\.url: 'http://elasticsearch:9200'\$" /etc/kibana/kibana.yml
ENV PATH=/usr/share/kibana/bin:$PATH \
    ENTRYPOINTS_DIR=/opt/qnib/entry
#ARG LOGTRAIL_VER=0.1.14
#RUN kibana-plugin install https://github.com/sivasamyk/logtrail/releases/download/${LOGTRAIL_VER}/logtrail-${KIBANA_VERSION}-${LOGTRAIL_VER}.zip
RUN apt-get update \
 && apt-get install -y curl \
 && rm -rf /var/lib/apt/lists/*
COPY opt/healthchecks/20-kibana.sh /opt/healthchecks/
HEALTHCHECK --interval=5s --retries=15 --timeout=1s \
  CMD /usr/local/bin/healthcheck.sh
CMD ["kibana"]
COPY opt/qnib/entry/* /opt/qnib/entry/
