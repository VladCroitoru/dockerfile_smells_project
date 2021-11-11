#
# Copyright 2017 Apereo Foundation (AF) Licensed under the
# Educational Community License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may
# obtain a copy of the License at
#
#     http://opensource.org/licenses/ECL-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an "AS IS"
# BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing
# permissions and limitations under the License.
#

#
# Step 1: Build the image
# $ docker build -f Dockerfile -t oae-cassandra:latest .
# Step 2: Run image
# $ docker run -it --name=cassandra --net=host oae-cassandra:latest
#
FROM openjdk:8-jre-alpine
LABEL Name=OAE-Cassandra 
LABEL Author=ApereoFoundation 
LABEL Email=oae@apereo.org

#
# Forked and adapted from official cassandra image
# available on https://hub.docker.com/_/cassandra/
# and
# https://hub.docker.com/r/nebo15/alpine-cassandra/~/dockerfile/
#

# Important! Update this no-op ENV variable when this Dockerfile # is updated with the current date. It will force refresh of all # of the base images and things like `apt-get update` won't be using # old cached versions when the Dockerfile is built.
ENV REFRESHED_AT=2016-10-14
ENV	LANG=en_US.UTF-8 
ENV	TERM=xterm
ENV	HOME=/ 
# Install gosu 
ENV GOSU_VERSION=1.10 
RUN set -x && \
apk add --no-cache --virtual .gosu-deps \
  dpkg \
  gnupg \
  openssl && \
  dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" && \
  wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch" && \
  wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc" && \
  export GNUPGHOME="$(mktemp -d)" && \
  gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 && \
  gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu && \
  rm -r /usr/local/bin/gosu.asc && \
  chmod +x /usr/local/bin/gosu && \
  gosu nobody true && \
  apk --purge del .gosu-deps

# Install Cassandra 
ENV CASSANDRA_VERSION=2.1.19
ENV CASSANDRA_HOME=/opt/cassandra \
  CASSANDRA_CONFIG=/etc/cassandra \ 
  CASSANDRA_PERSIST_DIR=/var/lib/cassandra \ 
  CASSANDRA_DATA=/var/lib/cassandra/data \ 
  CASSANDRA_COMMITLOG=/var/lib/cassandra/commitlog \ 
  CASSANDRA_LOG=/var/log/cassandra \ 
  CASSANDRA_USER=cassandra 

## Create data directories that should be used by Cassandra 
RUN mkdir -p ${CASSANDRA_DATA} \
  ${CASSANDRA_HOME} \
  ${CASSANDRA_CONFIG} \
  ${CASSANDRA_LOG} \
  ${CASSANDRA_COMMITLOG}

### Apache Cassandra 
RUN apk --update --no-cache add wget ca-certificates tar && \
  wget http://artfiles.org/apache.org/cassandra/${CASSANDRA_VERSION}/apache-cassandra-${CASSANDRA_VERSION}-bin.tar.gz -P /tmp && \
  tar -xvzf /tmp/apache-cassandra-${CASSANDRA_VERSION}-bin.tar.gz -C /tmp/ && \
  mv /tmp/apache-cassandra-${CASSANDRA_VERSION} ${CASSANDRA_HOME} && \
  rm -rf /tmp/apache-cassandra-${CASSANDRA_VERSION}-bin.tar.gz && \
  apk --purge del wget ca-certificates tar && \
  rm -rf /var/cache/apk/*

# Setup entrypoint and bash to execute it 
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN apk add --update --no-cache bash && \
  chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/bin/bash", "/docker-entrypoint.sh"]

# Change CASSANDRA_HOME ENV var to the correct folder
ENV CASSANDRA_HOME=/opt/cassandra/apache-cassandra-${CASSANDRA_VERSION} 

# Add default config 
RUN mv ${CASSANDRA_HOME}/conf/* ${CASSANDRA_CONFIG}
# COPY ./conf/* ${CASSANDRA_CONFIG}/
RUN chmod +x ${CASSANDRA_CONFIG}/*.sh

# https://issues.apache.org/jira/browse/CASSANDRA-11661 
RUN sed -ri 's/^(JVM_PATCH_VERSION)=.*/\1=25/' /etc/cassandra/cassandra-env.sh

# Add cassandra bin to PATH 
ENV PATH=$PATH:${CASSANDRA_HOME}/bin \ 
  CASSANDRA_CONF=${CASSANDRA_CONFIG} 
  
# Change directories ownership and access rights 
RUN adduser -D -s /bin/sh ${CASSANDRA_USER} && \
  chown -R ${CASSANDRA_USER}:${CASSANDRA_USER} ${CASSANDRA_HOME} \
  ${CASSANDRA_PERSIST_DIR} \
  ${CASSANDRA_DATA} \
  ${CASSANDRA_CONFIG} \
  ${CASSANDRA_LOG} \
  ${CASSANDRA_COMMITLOG} && \
  chmod 777 ${CASSANDRA_HOME} \
  ${CASSANDRA_PERSIST_DIR} \
  ${CASSANDRA_DATA} \
  ${CASSANDRA_CONFIG} \
  ${CASSANDRA_LOG} \
  ${CASSANDRA_COMMITLOG}
USER ${CASSANDRA_USER} 
WORKDIR ${CASSANDRA_HOME}

# Expose data volume 
VOLUME ${CASSANDRA_PERSIST_DIR}

# 7000: intra-node communication 
# 7001: TLS intra-node communication 
# 7199: JMX 
# 9042: CQL 
# 9160: thrift service 
EXPOSE 7000 7001 7199 9042 9160 

# debug
RUN ls -la ${CASSANDRA_HOME}/bin
# RUN echo $PATH

CMD ["cassandra", "-f", "JVM_OPTS='$JVM_OPTS -Dcassandra.unsafesystem=true'"]