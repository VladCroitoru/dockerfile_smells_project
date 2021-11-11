FROM openjdk:8-jre

ARG kafka_version=0.10.2.0
ARG scala_version=2.11

RUN apt-get update && apt-get install -y wget curl jq net-tools nano less

ENV KAFKA_VERSION=$kafka_version SCALA_VERSION=$scala_version

RUN curl --stderr /dev/null https://www.apache.org/dyn/closer.cgi\?as_json\=1 | jq -r '.preferred' > /tmp/mirror
ENV KAFKA_DISTR_URI=kafka/${KAFKA_VERSION}/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz

RUN wget -q "$(cat /tmp/mirror)$KAFKA_DISTR_URI" -O "/tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz"
RUN rm -rf /tmp/mirror

RUN tar xfz /tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz -C /opt && \
    rm /tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz && \
    ln -s /opt/kafka_${SCALA_VERSION}-${KAFKA_VERSION} /opt/kafka

COPY server_properties/* /opt/kafka/config/

WORKDIR /opt/kafka

#ENTRYPOINT bin/zookeeper-server-start.sh config/zookeeper.properties
