FROM mutterio/mini-java

ENV ELASTICSEARCH_VERSION 1.5.2
ENV APP_DIR=/opt/elasticsearch
RUN \
  mkdir -p /opt && \
  cd /tmp && \
  wget --progress=dot:mega https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-$ELASTICSEARCH_VERSION.tar.gz && \
  tar -xzf elasticsearch-$ELASTICSEARCH_VERSION.tar.gz && \
  rm -rf elasticsearch-$ELASTICSEARCH_VERSION.tar.gz && \
  mv elasticsearch-$ELASTICSEARCH_VERSION $APP_DIR &&\
  mkdir -p /data

ADD ./config/elasticsearch.yml $APP_DIR/config/elasticsearch.yml
ADD ./scripts/start.sh /start.sh

VOLUME ["/data"]

ENV JAVA_HOME /usr/lib/jvm/java-1.7-openjdk

EXPOSE 9200 9300
ENV CLUSTER_NAME mini-docker
ENV DATA_PATH /data/data
ENV DATA_LOGS /data/log
ENV ES_HEAP_SIZE 512m


CMD ["/start.sh"]
