FROM zookeeper

MAINTAINER Wurstmeister

RUN apk add --update unzip wget curl docker jq coreutils

ENV KAFKA_VERSION="0.10.0.1" SCALA_VERSION="2.11"
ADD download-kafka.sh /tmp/download-kafka.sh
RUN mkdir /opt && chmod a+x /tmp/download-kafka.sh && /tmp/download-kafka.sh && tar xfz /tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz -C /opt && rm /tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz

VOLUME ["/kafka"]

ENV KAFKA_HOME /opt/kafka_${SCALA_VERSION}-${KAFKA_VERSION}
ADD start-kafka.sh /usr/bin/start-kafka.sh
ADD broker-list.sh /usr/bin/broker-list.sh
ADD create-topics.sh /usr/bin/create-topics.sh
# The scripts need to have executable permission
RUN chmod a+x /usr/bin/start-kafka.sh && \
    chmod a+x /usr/bin/broker-list.sh && \
    chmod a+x /usr/bin/create-topics.sh
RUN apk --update add supervisor
COPY supervisor /etc/supervisor.d/
# Use "exec" form so that it runs as PID 1 (useful for graceful shutdown)
CMD ["supervisord", "-n", "-c", "/etc/supervisord.conf"]
