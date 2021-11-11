FROM java:8

MAINTAINER haha

ENV KAFKA_VERSION=0.10.0.0 KAFKA_SCALA_VERSION=2.11
ENV KAFKA_RELEASE_ARCHIVE kafka_${KAFKA_SCALA_VERSION}-${KAFKA_VERSION}.tgz

RUN mkdir /kafka /data /logs

ADD http://www.us.apache.org/dist/kafka/${KAFKA_VERSION}/${KAFKA_RELEASE_ARCHIVE} /tmp/

WORKDIR /tmp

RUN tar -zx -C /kafka --strip-components=1 -f ${KAFKA_RELEASE_ARCHIVE} && \
  rm -rf kafka_*

ADD zookeeper.properties /kafka/config/
ADD server.properties /kafka/config/
ADD start.sh /bin

# broker
EXPOSE 9092 2181
VOLUME [ "/data", "/logs" ]

CMD ["start.sh"]
