FROM java:8

ENV KAFKA_VERSION 0.10.1.0
ENV SCALA_VERSION 2.11
ENV WORKDIR /usr/share/
ENV KAFKA_HOME ${WORKDIR}/kafka

WORKDIR ${WORKDIR}

RUN curl http://www-us.apache.org/dist/kafka/${KAFKA_VERSION}/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz -o /tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz && \
    tar xfz /tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz -C ${WORKDIR} && \
    mv ${WORKDIR}/kafka_${SCALA_VERSION}-${KAFKA_VERSION} ${KAFKA_HOME} && \
    rm /tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz

ADD scripts/run.sh /usr/bin/start-kafka.sh

RUN chmod +x /usr/bin/start-kafka.sh

# 2181 is zookeeper, 9092 is kafka
EXPOSE 2181 9092

CMD ["start-kafka.sh"]


