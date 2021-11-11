#
# Elasticsearch Dockerfile
#
# https://github.com/dockerfile/elasticsearch
#

# Pull base image.
FROM dockerfile/java:oracle-java8

# Install supervisor
RUN apt-get update && \ 
  apt-get -y install build-essential python-setuptools && \
  easy_install supervisor

ENV ES_PKG_NAME elasticsearch-1.3.4

# Install Elasticsearch.
RUN \
  cd / && \
  wget https://download.elasticsearch.org/elasticsearch/elasticsearch/$ES_PKG_NAME.tar.gz && \
  tar xvzf $ES_PKG_NAME.tar.gz && \
  rm -f $ES_PKG_NAME.tar.gz && \
  mv /$ES_PKG_NAME /elasticsearch

# Define mountable directories.
#VOLUME ["/data"]

# Mount elasticsearch.yml config
# ADD config/elasticsearch.yml /elasticsearch/config/elasticsearch.yml

# Define working directory.
# WORKDIR /data

# Define default command.
#CMD ["/elasticsearch/bin/elasticsearch"]
CMD ["/bin/bash"]

# Expose ports.
#   - 9200: HTTP
#   - 9300: transport
EXPOSE 9200
EXPOSE 9300