ARG DOCKER_REGISTRY=docker.io
ARG DOCKER_IMG_TAG=":latest"
ARG DOCKER_IMG_HASH=""
FROM ${DOCKER_REGISTRY}/qnib/uplain-init${DOCKER_IMG_TAG}${DOCKER_IMG_HASH}

ARG CHRON_VER=1.3.7.0
LABEL influx.chronograf.version=${CHRON_VER}
# TODO: use docker secrets for INFLUXDB_PASSWORD
ENV INFLUXDB_URL=tasks.influxdb \
    INFLUXDB_PORT=8086

RUN apt-get update -q \
 && apt-get install -y -qq wget \
 && wget -qO - https://dl.influxdata.com/chronograf/releases/chronograf-${CHRON_VER}_linux_amd64.tar.gz |tar xfz - -C /opt/ \
 && mv /opt/chronograf-${CHRON_VER}-1/usr/bin/chronograf /usr/local/bin/
#COPY opt/qnib/entry/ /opt/qnib/entry/
COPY opt/qnib/influxdb/bin/start.sh /opt/qnib/influxdb/bin/
CMD ["/opt/qnib/influxdb/bin/start.sh"]
