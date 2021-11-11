#
# ElasticSearch Dockerfile
#
# https://github.com/dockerfile/elasticsearch
#

# Pull base image.
FROM multicloud/jre-8-oracle

ENV ES_PKG_NAME elasticsearch-1.6.0

# Install ElasticSearch.
RUN \
  cd / && \
  wget --progress=bar:force --no-check-certificate --retry-connrefused -t 5 https://download.elasticsearch.org/elasticsearch/elasticsearch/$ES_PKG_NAME.tar.gz && \
  tar xvzf $ES_PKG_NAME.tar.gz && \
  rm -f $ES_PKG_NAME.tar.gz && \
  mv /$ES_PKG_NAME /elasticsearch

# Define mountable directories.
VOLUME ["/data"]

# Mount elasticsearch.yml config
ADD config/elasticsearch.yml /elasticsearch/config/elasticsearch.yml

# Install Plugins.
RUN \
  /elasticsearch/bin/plugin -i mobz/elasticsearch-head && \
  /elasticsearch/bin/plugin -i lukas-vlcek/bigdesk && \
  /elasticsearch/bin/plugin -i lmenezes/elasticsearch-kopf && \
  /elasticsearch/bin/plugin -i elasticsearch/marvel/latest

# Define working directory.
WORKDIR /data

ADD entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

# Expose ports.
#   - 9200: HTTP
#   - 9300: transport
EXPOSE 9200
EXPOSE 9300

#Ignore /etc/hosts
RUN sed 's/^\(hosts:[\ ]*\)\(files\)\ \(dns\)$/\1\3 \2/' -i /etc/nsswitch.conf

#change logging level of discovery to trace
RUN sed 's/#discovery: TRACE/discovery: TRACE/' -i /elasticsearch/config/logging.yml
