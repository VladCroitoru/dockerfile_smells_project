### docker run -it --rm --name run-my-kafka -p 2181:2181 -p 9092:9092 daggerok/kafka:confluent-5.0.0

FROM openjdk:7u181-jre-alpine3.8
#FROM openjdk:8u171-jre-alpine3.8
LABEL MAINTAINER='Maksim Kostromin https://github.com/daggerok'
ARG CONFLUENT_VERSION='5.0'
ARG CONFLUENT_FULL_VERSION='5.0.0'
ARG SCALA_VERSION='2.11'
ARG CONFLUENT_DIRNAME="confluent-${CONFLUENT_FULL_VERSION}"
ARG CONFLUENT_BASE_URL='https://packages.confluent.io/archive'
ARG CONFLUENT_ARCHIVE_ARG="confluent-oss-${CONFLUENT_FULL_VERSION}-${SCALA_VERSION}.zip"
ARG CONFLUENT_URL_ARG="${CONFLUENT_BASE_URL}/${CONFLUENT_VERSION}/${CONFLUENT_ARCHIVE_ARG}"
ARG ZOOKEEPER_PORT_ARG='2181'
ARG KAFKA_PORT_ARG='9092'
ARG JAVA_OPTS_ARG='\
-Djava.net.preferIPv4Stack=true \
-XX:+UnlockExperimentalVMOptions \
-XX:+UseCGroupMemoryLimitForHeap \
-XshowSettings:vm '
ENV KAFKA_PATH="/root/kafka"
ENV PATH="${KAFKA_PATH}/${CONFLUENT_DIRNAME}/bin:${PATH}" \
    CONFLUENT_HOME="${KAFKA_PATH}/${CONFLUENT_DIRNAME}" \
    JAVA_OPTS="${JAVA_OPTS} ${JAVA_OPTS_ARG}" \
    CONFLUENT_ARCHIVE=${CONFLUENT_ARCHIVE_ARG} \
    ZOOKEEPER_PORT=${ZOOKEEPER_PORT_ARG} \
    CONFLUENT_URL=${CONFLUENT_URL_ARG} \
    KAFKA_PORT=${KAFKA_PORT_ARG}
WORKDIR ${KAFKA_PATH}
RUN apk add --no-cache --upgrade --update bash curl unzip lsof \
 && curl ${CONFLUENT_URL}  --silent --output /tmp/${CONFLUENT_ARCHIVE} \
 && unzip -q -d ./ /tmp/${CONFLUENT_ARCHIVE} \
 && apk del unzip wget \
 && apk cache clean || echo 'no cache found.' \
 && rm -rf  /tmp/* \
            /var/cache/apk/* \
            ${CONFLUENT_HOME}/src \
            ${CONFLUENT_HOME}/share/doc \
            ${CONFLUENT_HOME}/bin/windows \
 && echo 'for topic in $(echo ${KAFKA_TOPICS:-ololo,trololo}|tr -s ","  " "); do \
            kafka-topics --create \
              --zookeeper 127.0.0.1:${ZOOKEEPER_PORT} \
              --replication-factor 1 \
              --partitions 1 \
              --topic ${topic} ; \
          done' > ${CONFLUENT_HOME}/bin/create-kafka-topics \
 && chmod +x ${CONFLUENT_HOME}/bin/create-kafka-topics
CMD /bin/bash
ENTRYPOINT confluent start kafka \
         ; create-kafka-topics & confluent log zookeeper -f & confluent log kafka -f
EXPOSE ${KAFKA_PORT} ${ZOOKEEPER_PORT}
HEALTHCHECK \
  --timeout=1s \
  --retries=33 \
  CMD (test `lsof -i:${KAFKA_PORT}|awk '{print $2}'|wc -l` -ge 1 \
    && test `lsof -i:${ZOOKEEPER_PORT}|awk '{print $2}'|wc -l` -ge 1) \
    || exit 1

### you can use next docker-compose ###
#
# version: '2.1'
# services:
#   kafka:
#     image: daggerok/kafka:confluent-5.0.0
#     environment:
#       KAFKA_TOPICS: orders,invoices
#     ports:
#     - '2181:2181'
#     - '9092:9092'
#     networks: [backing-services]
# networks:
#   backing-services:
#     driver: bridge
#
#######################################

#################################################################################
# https://www.confluent.io/previous-versions/                                   #
# https://docs.confluent.io/current/installation/versions-interoperability.html #
#################################################################################

### no docker images for these options...

########################################################################
# https://packages.confluent.io/archive/1.0/confluent-1.0-2.11.5.zip   #
# https://packages.confluent.io/archive/1.0/confluent-1.0.1-2.11.5.zip #
# https://packages.confluent.io/archive/1.0/confluent-1.0.1-2.10.4.zip #
########################################################################

########################################################################
# https://packages.confluent.io/archive/2.0/confluent-2.0.0-2.10.5.zip #
# https://packages.confluent.io/archive/2.0/confluent-2.0.0-2.11.7.zip #
# https://packages.confluent.io/archive/2.0/confluent-2.0.1-2.10.5.zip #
# https://packages.confluent.io/archive/2.0/confluent-2.0.1-2.11.7.zip #
########################################################################

##########################################################################
# https://packages.confluent.io/archive/3.0/confluent-oss-3.0.0-2.10.zip #
# https://packages.confluent.io/archive/3.0/confluent-oss-3.0.0-2.11.zip #
# https://packages.confluent.io/archive/3.0/confluent-oss-3.0.1-2.10.zip #
# https://packages.confluent.io/archive/3.0/confluent-oss-3.0.1-2.11.zip #
##########################################################################

##########################################################################
# https://packages.confluent.io/archive/3.1/confluent-oss-3.1.1-2.10.zip #
# https://packages.confluent.io/archive/3.1/confluent-oss-3.1.1-2.11.zip #
# https://packages.confluent.io/archive/3.1/confluent-oss-3.1.2-2.10.zip #
# https://packages.confluent.io/archive/3.1/confluent-oss-3.1.2-2.11.zip #
##########################################################################

##########################################################################
# https://packages.confluent.io/archive/3.2/confluent-oss-3.2.0-2.10.zip #
# https://packages.confluent.io/archive/3.2/confluent-oss-3.2.0-2.11.zip #
# https://packages.confluent.io/archive/3.2/confluent-oss-3.2.1-2.10.zip #
# https://packages.confluent.io/archive/3.2/confluent-oss-3.2.1-2.11.zip #
# https://packages.confluent.io/archive/3.2/confluent-oss-3.2.2-2.10.zip #
# https://packages.confluent.io/archive/3.2/confluent-oss-3.2.2-2.11.zip #
# https://packages.confluent.io/archive/3.2/confluent-oss-3.2.3-2.10.zip #
# https://packages.confluent.io/archive/3.2/confluent-oss-3.2.3-2.11.zip #
# https://packages.confluent.io/archive/3.2/confluent-oss-3.2.4-2.10.zip #
# https://packages.confluent.io/archive/3.2/confluent-oss-3.2.4-2.11.zip #
##########################################################################

### only since version 3.3 confluent CLI was added

##########################################################################
# https://packages.confluent.io/archive/3.3/confluent-oss-3.3.0-2.11.zip #
# https://packages.confluent.io/archive/3.3/confluent-oss-3.3.1-2.11.zip #
# https://packages.confluent.io/archive/3.3/confluent-oss-3.3.2-2.11.zip #
##########################################################################

##########################################################################
# https://packages.confluent.io/archive/4.0/confluent-oss-4.0.0-2.11.zip #
# https://packages.confluent.io/archive/4.0/confluent-oss-4.0.1-2.11.zip #
# https://packages.confluent.io/archive/4.0/confluent-oss-4.0.2-2.11.zip #
##########################################################################

##########################################################################
# https://packages.confluent.io/archive/4.1/confluent-oss-4.1.0-2.11.zip #
# https://packages.confluent.io/archive/4.1/confluent-oss-4.1.1-2.11.zip #
# https://packages.confluent.io/archive/4.1/confluent-oss-4.1.2-2.11.zip #
##########################################################################

##########################################################################
# https://packages.confluent.io/archive/5.0/confluent-oss-5.0.0-2.11.zip #
##########################################################################
