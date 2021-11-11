FROM anapsix/alpine-java:8

MAINTAINER Francois Reignat <freignat@axway.com>

RUN apk update && apk --no-cache add gpgme openjdk8-jre

ENV KAFKA_VERSION="0.10.0.1"
ENV SCALA_VERSION="2.11"

LABEL name="kafka" version="$KAFKA_VERSION"


RUN wget "http://mirror.cc.columbia.edu/pub/software/apache/kafka/$KAFKA_VERSION/kafka_${SCALA_VERSION}-$KAFKA_VERSION.tgz" -O /tmp/kafka.tgz \
&& mkdir -p /opt \
&& tar -xvzf /tmp/kafka.tgz -C /opt \
&& mv /opt/kafka_${SCALA_VERSION}-$KAFKA_VERSION /opt/kafka && rm /tmp/kafka.tgz

WORKDIR /opt/kafka

COPY ./check.sh /opt/kafka/bin/check.sh
COPY ./server.properties /opt/kafka/config/server.properties


ENV ZOOKEEPER_CONNECT localhost:2181
ENV KAFKA_IP=localhost

EXPOSE 9092

HEALTHCHECK --interval=5s --timeout=10s --retries=12 CMD /opt/kafka/bin/check.sh

CMD ["/opt/kafka/bin/kafka-server-start.sh", "/opt/kafka/config/server.properties"]
