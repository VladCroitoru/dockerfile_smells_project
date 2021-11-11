# Keyinsp Custom Elasticsearch image
FROM docker.elastic.co/elasticsearch/elasticsearch:6.0.0

LABEL MAINTAINER=mike@whatsmycut.com

# Override config, otherwise plug-in install will fail
ADD config /elasticsearch/config

# Set environment
ENV DISCOVERY_SERVICE elasticsearch-discovery

# Kubernetes requires swap is turned off, so memory lock is redundant
ENV MEMORY_LOCK false

RUN bin/elasticsearch-plugin remove x-pack
RUN bin/elasticsearch-plugin install x-pack

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
