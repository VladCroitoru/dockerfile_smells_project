# Builds an image for Apache Kafka 0.8 from binary distribution.
#
# The netflixoss/java base image runs Oracle Java 7 installed atop the
# ubuntu:trusty (14.04) official image. Docker's official java images are
# OpenJDK-only currently, and the Kafka project, Confluent, and most other
# major Java projects test and recommend Oracle Java for production for optimal
# performance.
#
# Thanks to https://hub.docker.com/r/ches/kafka/ for a solid skeleton
#
FROM netflixoss/java:8
MAINTAINER Julien Rottenberg <julien@rottenberg.info>

EXPOSE 9092 2181

# The Scala 2.10 build is currently recommended by the project.
ENV KAFKA_VERSION=0.8.2.1 KAFKA_SCALA_VERSION=2.10
ENV KAFKA_RELEASE_ARCHIVE kafka_${KAFKA_SCALA_VERSION}-${KAFKA_VERSION}.tgz



RUN apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y \
    ca-certificates

# Download Kafka binary distribution
RUN wget -qP /tmp http://www.us.apache.org/dist/kafka/${KAFKA_VERSION}/${KAFKA_RELEASE_ARCHIVE} && \
    wget -qP /tmp/  https://dist.apache.org/repos/dist/release/kafka/${KAFKA_VERSION}/${KAFKA_RELEASE_ARCHIVE}.md5

# Check artifact digest integrity
RUN echo VERIFY CHECKSUM: && \
  gpg --print-md MD5 /tmp/${KAFKA_RELEASE_ARCHIVE} 2>/dev/null && \
  cat /tmp/${KAFKA_RELEASE_ARCHIVE}.md5


# Install Kafka to /kafka
WORKDIR /kafka

RUN tar -zx -C /kafka --strip-components=1 -f /tmp/${KAFKA_RELEASE_ARCHIVE} && \
    rm -rf /tmp/kafka_* && \
    mkdir -p /logs/zookepper /logs/kafka && \
    ln -s  /logs/zookepper /tmp/zookeeper && \
    ln -s /logs/kafka /tmp/kafka-logs && \
    ln -s /logs/kafka logs && \
    sed -i s/log.retention.hours=168/log.retention.hours=1/g config/server.properties

RUN chown -R nobody: /logs

VOLUME [ "/logs" ]

ADD  start.sh /start.sh

CMD ["/start.sh"]
