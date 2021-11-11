FROM java:8
MAINTAINER Alberto Grespan <alberto.grespan@full360.com>

# Export the VOLTDB_VERSION, VOLTDB_DIR and binaries to the PATH
ENV VOLTDB_VERSION 6.4
ENV VOLTDB_DIR /usr/local/opt/voltdb
ENV PATH $PATH:$VOLTDB_DIR/$VOLTDB_VERSION/bin

# Build and cleanup everything after compilation
WORKDIR /tmp
RUN set -ex \
  && buildDeps=' \
      ant \
      build-essential \
      curl \
      ccache \
      cmake \
  ' \
  && apt-get update  \
  && apt-get install -y --no-install-recommends $buildDeps \
  && rm -rf /var/lib/apt/lists/* \
  && curl -fSL https://github.com/VoltDB/voltdb/archive/voltdb-${VOLTDB_VERSION}.tar.gz | tar zx \
  && cd /tmp/voltdb-voltdb-${VOLTDB_VERSION} \
  && ant -Djmemcheck=NO_MEMCHECK \
  && mkdir -p ${VOLTDB_DIR}/${VOLTDB_VERSION} \
  && cd ${VOLTDB_DIR}/${VOLTDB_VERSION} \
  && for file in LICENSE README.md README.thirdparty bin bundles doc examples lib third_party/python tools version.txt voltdb; do \
      cp -R /tmp/voltdb-voltdb-${VOLTDB_VERSION}/${file} .; done \
  && mkdir -p third_party \
  && mv python third_party \
  && apt-get purge -y --auto-remove $buildDeps \
  && rm -rf /tmp/voltdb-voltdb-${VOLTDB_VERSION}

# Our default VoltDB work dir
WORKDIR /usr/local/var/voltdb

# Exposed ports:
# Client Port 21212
# Admin Port 21211
# JMX Port 9090
# Web Interface Port (httpd) 8080
# Zookeeper port 7181
# Replication Port 5555
# Log Port 4560
# Internal Server Port 3021
EXPOSE 21212 21211 9090 8080 7181 5555 4560 3021

CMD ["voltdb", "create", "--ignore=thp"]
