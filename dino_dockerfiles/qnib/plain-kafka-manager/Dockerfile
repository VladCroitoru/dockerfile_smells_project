ARG DOCKER_REGISTRY=docker.io
ARG DOCKER_IMAGE_NAME="alplain-openjdk8-sbt"
ARG DOCKER_IMG_TAG=":0.13.15"
ARG DOCKER_IMG_HASH=""
ARG DOCKER2_IMG_TAG=":2018-09-10_09-03_7257f5145fa3"
ARG DOCKER2_IMG_HASH=""
FROM ${DOCKER_REGISTRY}/qnib/${DOCKER_IMAGE_NAME}${DOCKER_IMG_TAG}${DOCKER_IMG_HASH} AS build

ARG KM_VER=1.3.3.18
ARG SCALA_VER=2.11
RUN apk --no-cache add wget \
 && wget -qO- https://github.com/yahoo/kafka-manager/archive/${KM_VER}.tar.gz |tar xfz - -C /opt/ \
 && mv /opt/kafka-manager-${KM_VER} /opt/kafka-manager
RUN cd /opt/kafka-manager/ \
 && sbt 'set test in assembly := {}' clean assembly

FROM ${DOCKER_REGISTRY}/qnib/alplain-openjre8-prometheus${DOCKER2_IMG_TAG}${DOCKER2_IMG_HASH}
ARG KM_VER=1.3.3.18
ARG SCALA_VER=2.11
LABEL kafka-manager.version=${SCALA_VER}-${KM_VER}
ENV ZOOKEEPER_HOSTS=localhost \
    ENTRYPOINTS_DIR=/opt/qnib/entry
COPY --from=build /opt/kafka-manager/target/scala-${SCALA_VER}/kafka-manager-assembly-${KM_VER}.jar /opt/kafka-manager/kafka-manager-assembly.jar
COPY --from=build  /opt/kafka-manager/conf/ /opt/kafka-manager/conf/
COPY opt/qnib/kafka/manager/bin/start.sh \
    opt/qnib/kafka/manager/bin/healthcheck.sh \
    /opt/qnib/kafka/manager/bin/
COPY opt/qnib/entry/30-kafka-manager.sh \
    /opt/qnib/entry/
COPY opt/qnib/kafka/manager/conf/application.conf \
    /opt/qnib/kafka/manager/conf/
CMD ["/opt/qnib/kafka/manager/bin/start.sh"]
