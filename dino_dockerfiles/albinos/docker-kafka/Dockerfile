# Using alternative alpine image because default alpine glibc is not compatible
# with jdk8
FROM frolvlad/alpine-oraclejdk8:slim
MAINTAINER Albin Gilles <gilles.albin@gmail.com>
ENV REFRESHED_AT 2016-09-15

# Kafka versionning
ENV SCALA_VERSION 2.11
ENV KAFKA_VERSION 0.10.0.1
ENV KAFKA_FULL_NAME "kafka_$SCALA_VERSION-$KAFKA_VERSION"

# Kafka releaser key
ENV GPG_KEY AB55EF5C

# Install bash
RUN apk add --no-cache bash

# Install Kafka
RUN set -x \
    && apk add --no-cache --virtual gnupg \
    && export GNUPGHOME="$(mktemp -d)" \
    && wget -q "http://www.apache.org/dist/kafka/$KAFKA_VERSION/$KAFKA_FULL_NAME.tgz" \
    && wget -q "http://www.apache.org/dist/kafka/$KAFKA_VERSION/$KAFKA_FULL_NAME.tgz.asc" \
    && export GNUPGHOME="$(mktemp -d)" \
    && gpg --keyserver ha.pool.sks-keyservers.net --recv-key "$GPG_KEY" \
    && gpg --batch --verify "$KAFKA_FULL_NAME.tgz.asc" "$KAFKA_FULL_NAME.tgz" \
    && mkdir /opt \
    && tar xfz "$KAFKA_FULL_NAME.tgz" -C /opt \
    && rm -rf "$KAFKA_FULL_NAME.tgz" "$KAFKA_FULL_NAME.tgz.asc" "$GNUPGHOME"

# Kafka persistence
RUN mkdir /kafka
RUN mkdir /kafka/config
VOLUME ["/kafka"]

# Kafka configuration
ENV KAFKA_SERVER_PROPERTIES "/kafka/config/server.properties"
ENV KAFKA_HOME "/opt/$KAFKA_FULL_NAME"

# Kafka port
EXPOSE 9092

# Run Kafka
COPY ./kafka_entrypoint.sh /usr/bin/kafka_entrypoint.sh
COPY ./kafka_server.properties /kafka/config/server.properties
ENTRYPOINT ["/usr/bin/kafka_entrypoint.sh"]
