FROM confluentinc/cp-base

EXPOSE 2181 2888 3888 9092

MAINTAINER james@notjam.es

ENV ZOOKEEPER_CLIENT_PORT=2181
ENV KAFKA_ZOOKEEPER_CONNECT=127.0.0.1:2181
ENV KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://:9092
ENV KAFKA_BROKER_ID=1
ENV KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1

ENV COMPONENT_ZOOKEEPER=zookeeper
ENV COMPONENT_KAFKA=kafka

RUN apt-get update \
    && echo "===> installing supervisord..." \
    && apt-get install -y supervisor \
    \
    && echo "===> installing ${COMPONENT_ZOOKEEPER}..." \
    && apt-get install -y confluent-kafka-${SCALA_VERSION}=${KAFKA_VERSION}${CONFLUENT_PLATFORM_LABEL}-${CONFLUENT_DEB_VERSION} \
    \
    && echo "===> clean up ..."  \
    && apt-get clean && rm -rf /tmp/* /var/lib/apt/lists/* \
    \
    && echo "===> Setting up ${COMPONENT_ZOOKEEPER} dirs" \
    && mkdir -p /var/lib/${COMPONENT_ZOOKEEPER}/data /var/lib/${COMPONENT_ZOOKEEPER}/log /etc/${COMPONENT_ZOOKEEPER}/secrets \
    && chmod -R ag+w /etc/${COMPONENT_ZOOKEEPER} /var/lib/${COMPONENT_ZOOKEEPER}/data /var/lib/${COMPONENT_ZOOKEEPER}/log /etc/${COMPONENT_ZOOKEEPER}/secrets \
    \
    && echo "===> clean up ..."  \
    && apt-get clean && rm -rf /tmp/* /var/lib/apt/lists/* \
    \
		&& echo "===> Setting up ${COMPONENT_KAFKA} dirs..." \
   	&& mkdir -p /var/lib/${COMPONENT_KAFKA}/data /etc/${COMPONENT_KAFKA}/secrets\
    && chmod -R ag+w /etc/${COMPONENT_KAFKA} /var/lib/${COMPONENT_KAFKA}/data /etc/${COMPONENT_KAFKA}/secrets

COPY kafka /etc/confluent/docker/kafka/
COPY zookeeper /etc/confluent/docker/zookeeper/

COPY supervisor-conf.d/* /etc/supervisor/conf.d/

COPY healthcheck.sh /

HEALTHCHECK --interval=30s --timeout=3s CMD /healthcheck.sh

CMD ["supervisord", "-n"]
