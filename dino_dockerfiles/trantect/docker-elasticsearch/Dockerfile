FROM jeanblanchard/busybox-java:7

ENV ES_VERSION 1.4.4

# Install ElasticSearch.
RUN \
  cd / && \
  wget http://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-$ES_VERSION.tar.gz && \
  gzip -d $ES_PKG_NAME.tar.gz && \
  tar xvf $ES_PKG_NAME.tar && \
  rm -f $ES_PKG_NAME.tar && \
  mv /$ES_PKG_NAME /elasticsearch

# Define default command.
CMD ["/elasticsearch/bin/elasticsearch"]

# Expose ports.
#   - 9200: HTTP
#   - 9300: transport
EXPOSE 9200
EXPOSE 9300
