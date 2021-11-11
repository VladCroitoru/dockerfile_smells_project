# howgood/elasticsearch
# Pull base image.
FROM java:7

ENV ES_VERSION 1.3.2

# Install ElasticSearch.
RUN mkdir /usr/share/elasticsearch && \
    cd /usr/share/elasticsearch && \
    curl -SL "https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-$ES_VERSION.tar.gz" \
      | tar zx --strip-components=1

VOLUME ["/var/log/elasticsearch", "/var/lib/elasticsearch"]

# 9200: HTTP
# 9300: transport
EXPOSE 9200 9300

ENTRYPOINT ["/usr/share/elasticsearch/bin/elasticsearch"]
CMD ["-Des.default.path.logs=/var/log/elasticsearch", "-Des.default.path.data=/var/lib/elasticsearch"]
