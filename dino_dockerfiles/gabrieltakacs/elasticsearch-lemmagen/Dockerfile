FROM java:8u92-jre-alpine
MAINTAINER Gabriel Takács <gtakacs@gtakacs.sk>

# Install common utilities
RUN apk update && \
    apk upgrade -U && \
    apk add bash fish vim git grep sed curl wget tar gzip pcre perl

# Download and install Elasticsearch
ENV ES_VERSION=2.3.2
ADD https://download.elasticsearch.org/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/$ES_VERSION/elasticsearch-$ES_VERSION.tar.gz /tmp/es.tgz
RUN cd /usr/share && \
  tar xf /tmp/es.tgz && \
  rm /tmp/es.tgz

ADD start /start
RUN chmod a+x /start

ENV ES_HOME=/usr/share/elasticsearch-$ES_VERSION
ENV OPTS=-Dnetwork.host=_non_loopback_
ENV DEFAULT_ES_USER=elasticsearch
RUN ln -s /usr/share/elasticsearch-$ES_VERSION /usr/share/elasticsearch

# Add elasticsearch user
RUN adduser -S -s /bin/sh $DEFAULT_ES_USER

# Add lemmagen configuration file
ADD ./config/settings.yml /usr/share/elasticsearch/config/hunspell/sk_SK/settings.yml

# Download hunspell-sk files
ENV HUNSPELL_SK_BASE https://github.com/essential-data/hunspell-sk/releases/download/1.1/
ENV HUNSPELL_SK_FILE hunspell-sk_SK-lemma-ascii.tar.gz
ADD ${HUNSPELL_SK_BASE}/${HUNSPELL_SK_FILE} /usr/share/elasticsearch/config/hunspell/
RUN tar xvzf /usr/share/elasticsearch/config/hunspell/${HUNSPELL_SK_FILE}

# Install lemmagen
RUN cd /usr/share/elasticsearch-2.3.2 && \
   ./bin/plugin install https://github.com/vhyza/elasticsearch-analysis-lemmagen/releases/download/v$ES_VERSION/elasticsearch-analysis-lemmagen-$ES_VERSION-plugin.zip

EXPOSE 9200
EXPOSE 9300

WORKDIR $ES_HOME
CMD ["/start"]

