# VERSION 1.0
# AUTHOR: Matthieu "Puckel_" Roisil
# DESCRIPTION: Basic Elasticsearch container
# BUILD: docker build --rm -t puckel/docker-elasticsearch
# SOURCE: https://github.com/puckel/docker-elasticsearch

FROM java:8
MAINTAINER Puckel_

# Never prompts the user for choices on installation/configuration of packages
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux
# Work around initramfs-tools running on kernel 'upgrade': <http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=594189>
ENV INITRD No

ENV ES_PKG_NAME elasticsearch-1.7.1

# Install ElasticSearch.
RUN \
  cd / \
  && curl -sL https://download.elastic.co/elasticsearch/elasticsearch/$ES_PKG_NAME.tar.gz |tar xz \
  && rm -f $ES_PKG_NAME.tar.gz \
  && mv /$ES_PKG_NAME /elasticsearch

# Mount elasticsearch.yml config
ADD config/elasticsearch.yml /elasticsearch/config/elasticsearch.yml

# Install head plugin
RUN /elasticsearch/bin/plugin -install mobz/elasticsearch-head

# Define mountable directories.
VOLUME ["/data"]

# Define working directory.
WORKDIR /data

# Define default command.
CMD ["/elasticsearch/bin/elasticsearch"]

# Expose ports.
#   - 9200: HTTP
#   - 9300: transport
EXPOSE 9200
EXPOSE 9300
