ARG DOCKER_REGISTRY=docker.io
FROM ${DOCKER_REGISTRY}/qnib/alplain-init

ARG PROM_URL=https://github.com/prometheus/prometheus/releases/download
ARG PROM_VER=2.3.1
ARG PROM_ARCH=linux-amd64
LABEL prometheus.version=${PROM_VER}
COPY opt/qnib/prometheus/prometheus.yml /opt/qnib/prometheus/
COPY opt/entry/*.sh /opt/entry/
RUN adduser -s /sbin/nologin -D prometheus
CMD ENTRY_USER=prometheus
RUN apk --no-cache add wget \
 && wget -qO- ${PROM_URL}/v${PROM_VER}/prometheus-${PROM_VER}.${PROM_ARCH}.tar.gz |tar xfz - -C /opt/ \
 && mv /opt/prometheus-${PROM_VER}.${PROM_ARCH}/ /opt/prometheus
VOLUME ["/data/prometheus"]
CMD ["/opt/prometheus/prometheus","--config.file=/etc/prometheus.yml","--storage.tsdb.path=/data/prometheus","--web.listen-address=0.0.0.0:9090"]
