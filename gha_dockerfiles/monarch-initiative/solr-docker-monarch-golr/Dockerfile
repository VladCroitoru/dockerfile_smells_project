FROM maven:3.6.0-jdk-8-slim
# use bash
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

ARG CURIE_MAP='https://archive.monarchinitiative.org/beta/translationtable/curie_map.yaml'
ARG SOLR_UID='1006'

# Install git and wget
RUN apt-get -y update && apt-get install -y git wget

RUN adduser --disabled-password --uid "$SOLR_UID" solr

WORKDIR /data
RUN chown solr:solr /data

USER solr

ENV MAVEN_CONFIG "$WORKDIR/.m2"

VOLUME /solr

ADD files/functions.inc /data
ADD files/logback.xml /data
ADD files/run.sh /data
ADD files/solrconfig.xml /data
ADD files/golr-config.yaml /data

RUN git clone https://github.com/SciGraph/SciGraph.git /data/scigraph
RUN git clone https://github.com/SciGraph/golr-loader.git /data/golr-loader
RUN git clone https://github.com/monarch-initiative/monarch-cypher-queries.git /data/monarch-cypher-queries
RUN git clone https://github.com/berkeleybop/golr-schema /data/golr-schema

RUN cd /data/scigraph && mvn install -DskipTests -DskipITs
RUN cd /data/golr-loader && mvn install -Dmaven.test.skip
RUN cd /data/monarch-cypher-queries && mvn install
RUN cd /data/golr-schema && mvn install

RUN wget http://archive.apache.org/dist/lucene/solr/6.2.1/solr-6.2.1.tgz -P /data
RUN cd /data && tar xzfv /data/solr-6.2.1.tgz

RUN source /data/functions.inc && getGraphConfiguration /data/graph $CURIE_MAP > graph.yaml

CMD /data/run.sh
