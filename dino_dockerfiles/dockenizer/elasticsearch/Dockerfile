FROM dockenizer/alpine
MAINTAINER Jacques Moati <jacques@moati.net>

ENV ELASTICSEARCH_VERSION=5.1.1
ENV GOSU_VERSION 1.7

RUN apk --update add curl openjdk8-jre && \
  curl -o /usr/local/bin/gosu -sSL "https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-amd64" && \
  chmod +x /usr/local/bin/gosu && \
  curl -o elasticsearch-${ELASTICSEARCH_VERSION}.tar.gz -sSL https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-${ELASTICSEARCH_VERSION}.tar.gz && \
  tar -xzf elasticsearch-${ELASTICSEARCH_VERSION}.tar.gz && \
  mv elasticsearch-${ELASTICSEARCH_VERSION} /usr/share/elasticsearch && \
  mkdir -p /usr/share/elasticsearch/data /usr/share/elasticsearch/logs /usr/share/elasticsearch/config/scripts && \
  adduser -DH -s /sbin/nologin elasticsearch && \
  chown -R elasticsearch:elasticsearch /usr/share/elasticsearch && \

  apk del --purge curl && \
  rm -rf /var/cache/apk/* && \
  rm elasticsearch-${ELASTICSEARCH_VERSION}.tar.gz

ENV PATH /usr/share/elasticsearch/bin:$PATH

WORKDIR /usr/share/elasticsearch
VOLUME /usr/share/elasticsearch/data

COPY config ./config
COPY docker-entrypoint.sh /

RUN chmod +x /docker-entrypoint.sh

EXPOSE 9200 9300
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["elasticsearch"]