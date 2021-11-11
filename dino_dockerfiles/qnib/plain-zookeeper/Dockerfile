ARG DOCKER_REGISTRY=docker.io
ARG DOCKER_IMG_TAG=":2019-01-28.2"
ARG DOCKER_IMG_HASH="@sha256:bac2b14174d7908eb94f6b4d247ff765d0488397227a8a17e3ebeac6ce3d5d18"
FROM ${DOCKER_REGISTRY}/qnib/alplain-openjre8-prometheus${DOCKER_IMG_TAG}${DOCKER_IMG_HASH}

ENV ENTRYPOINTS_DIR=/opt/qnib/entry \
    PROMETHEUS_JMX_PROFILE=zookeeper \
    PATH=/opt/zookeeper/bin:${PATH} \
    ZOO_USER=zookeeper \
    ZOO_CONF_DIR=/conf \
    ZOO_DATA_DIR=/data \
    ZOO_DATA_LOG_DIR=/datalog \
    ZOO_PORT=2181 \
    ZOO_TICK_TIME=2000 \
    ZOO_INIT_LIMIT=5 \
    ZOO_SYNC_LIMIT=2
COPY opt/prometheus/jmx/zookeeper.yml /opt/prometheus/jmx/
# Add a user and make dirs
RUN set -x \
    && adduser -D "$ZOO_USER" \
    && mkdir -p "$ZOO_DATA_LOG_DIR" "$ZOO_DATA_DIR" "$ZOO_CONF_DIR" \
    && chown "$ZOO_USER:$ZOO_USER" "$ZOO_DATA_LOG_DIR" "$ZOO_DATA_DIR" "$ZOO_CONF_DIR"

ARG DISTRO_NAME=zookeeper-3.4.13
ARG DURL=http://www.apache.org/dist/zookeeper

# Download Apache Zookeeper, verify its PGP signature, untar and clean up
RUN apk add --no-cache --virtual .build-deps gnupg \
 && echo
RUN echo \
    && mkdir -p /opt/zookeeper/ \
    && wget -qO - "${DURL}/$DISTRO_NAME/$DISTRO_NAME.tar.gz" |tar xfz - --strip-components=1 -C /opt/zookeeper/ \
    && apk del .build-deps

WORKDIR $DISTRO_NAME
VOLUME ["$ZOO_DATA_DIR", "$ZOO_DATA_LOG_DIR"]

EXPOSE $ZOO_PORT 2888 3888

COPY opt/zookeeper/conf/zoo.cfg /conf/
ENV PATH=$PATH:/$DISTRO_NAME/bin \
    ZOOCFGDIR=$ZOO_CONF_DIR
COPY opt/qnib/zookeeper/bin/start.sh /opt/qnib/zookeeper/bin/
CMD ["/opt/qnib/zookeeper/bin/start.sh"]
