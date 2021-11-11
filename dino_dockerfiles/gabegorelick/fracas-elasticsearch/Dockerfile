###############################################################################
# Dockerfile for Elasticsearch. Unlike most other Elasticsearch Dockerfiles,
# this one uses debian:jessie to minimize size, OpenJDK instead of Oracle's
# JRE, and checks SHA sums.
###############################################################################

FROM debian:jessie

MAINTAINER Gabe Gorelick, "https://github.com/gabegorelick"

RUN apt-get update \
  && apt-get install -y openjdk-7-jre-headless curl --no-install-recommends \
  && rm -rf /var/lib/apt/lists/*

ENV ELASTICSEARCH_DOWNLOAD_URL https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.4.0.tar.gz
ENV ELASTICSEARCH_DOWNLOAD_SHA1 728913722bc94dad4cb5e759a362f09dc19ed6fe

# Download and install elasticsearch. We don't use their debs because this is
# easier and we don't care about the package manager (this is Docker after all).
RUN set -x; \
  cd /tmp \
  && curl -sSL "$ELASTICSEARCH_DOWNLOAD_URL" -o elasticsearch.tar.gz \
  && echo "$ELASTICSEARCH_DOWNLOAD_SHA1 *elasticsearch.tar.gz" | sha1sum -c - \
  && mkdir -p /elasticsearch \
  && tar -xzf elasticsearch.tar.gz -C /elasticsearch --strip-components=1 \
  && rm -f elasticsearch.tar.gz \
  && apt-get purge -y curl \
  && apt-get autoremove -y

VOLUME ["/data"]

ADD elasticsearch.yml /elasticsearch/config/elasticsearch.yml

WORKDIR /data

CMD ["/elasticsearch/bin/elasticsearch"]

# HTTP
EXPOSE 9200

# Transport
EXPOSE 9300
