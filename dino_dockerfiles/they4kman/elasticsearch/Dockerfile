#
# Elasticsearch Dockerfile
#
# https://github.com/dockerfile/elasticsearch
#

# Pull base image.
FROM dockerfile/java:oracle-java8

ENV ES_PKG_NAME elasticsearch-2.0.0-SNAPSHOT
ENV ES_COMMIT 896e8657ea498c074e9b7661d71f698b5cd23e94
ENV MVN_PKG_NAME apache-maven-3.2.5

# Install Elasticsearch snapshot.
RUN \
  cd / && \
  wget http://psg.mtu.edu/pub/apache/maven/maven-3/3.2.5/binaries/$MVN_PKG_NAME-bin.tar.gz && \
  tar xvzf $MVN_PKG_NAME-bin.tar.gz && \
  rm -f $MVN_PKG_NAME-bin.tar.gz && \
  apt-get install build-essential && \
  wget https://github.com/elasticsearch/elasticsearch/archive/$ES_COMMIT.tar.gz && \
  tar xvzf $ES_COMMIT.tar.gz && \
  rm -f $ES_COMMIT.tar.gz && \
  cd /elasticsearch-$ES_COMMIT && \
  /$MVN_PKG_NAME/bin/mvn clean package -DskipTests && \
  cd /elasticsearch-$ES_COMMIT/target/releases/ && \
  tar xvzf $ES_PKG_NAME.tar.gz && \
  mv /elasticsearch-$ES_COMMIT/target/releases/$ES_PKG_NAME /elasticsearch && \
  rm -rf /$MVN_PKG_NAME /elasticsearch-$ES_COMMIT

# Define mountable directories.
VOLUME ["/data"]

# Mount elasticsearch.yml config
ADD config/elasticsearch.yml /elasticsearch/config/elasticsearch.yml

# Define working directory.
WORKDIR /data

# Define default command.
CMD ["/elasticsearch/bin/elasticsearch"]

# Expose ports.
#   - 9200: HTTP
#   - 9300: transport
EXPOSE 9200
EXPOSE 9300

