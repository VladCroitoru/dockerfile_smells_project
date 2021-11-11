FROM java:8-jre
MAINTAINER Eagle Chen <chygr1234@gmail.com>

ENV ES_VERSION="2.2.1"
ENV GOSU_VERSION="1.8"

# es needs non-root user to start

RUN cd /tmp && curl -OL https://github.com/medcl/elasticsearch-rtf/archive/${ES_VERSION}.zip && \
  unzip ${ES_VERSION}.zip -d /usr/share && rm /tmp/${ES_VERSION}.zip && \
  mv /usr/share/elasticsearch-rtf-${ES_VERSION} /usr/share/elasticsearch && \
  groupadd es && useradd -g es es && \
  for path in data config logs config/scripts; do mkdir -p "/usr/share/elasticsearch/$path"; done && \
  chown -R es:es /usr/share/elasticsearch && \
  curl -o /usr/local/bin/gosu -fsSL "https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-$(dpkg --print-architecture)" && \
  chmod +x /usr/local/bin/gosu

ENV PATH /usr/share/elasticsearch/bin:$PATH

VOLUME /usr/share/elasticsearch/data

VOLUME /usr/share/elasticsearch/logs

COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 9200 9300

CMD ["elasticsearch"]
