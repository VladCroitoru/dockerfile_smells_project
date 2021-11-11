FROM openjdk:alpine
MAINTAINER doggytty<doggytty@126.com>

ENV SCALA_VERSION=2.12 KAFKA_VERSION=0.10.2.1
ENV KAFKA_HOME=/usr/local/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION" \
    PATH=$PATH:/usr/local/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION"/bin

# Install Kafka, Zookeeper and other needed things
RUN apk update && apk upgrade && apk add bash && \
    wget -c http://apache.claz.org/kafka/"$KAFKA_VERSION"/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz -O /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz && \
    tar xfz /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz -C /usr/local  && \
    rm /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz

ADD docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
ADD config/* ${KAFKA_HOME}/config/

# 9092 is kafka
EXPOSE 9092
VOLUME /data
WORKDIR ${KAFKA_HOME}

CMD ["docker-entrypoint.sh"]

