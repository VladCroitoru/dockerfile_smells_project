#------------------------------------------------------------------------------
# Set the base image for subsequent instructions:
#------------------------------------------------------------------------------

FROM frolvlad/alpine-glibc:alpine-3.4
MAINTAINER Marc Villacorta Morera <marc.villacorta@gmail.com>

#------------------------------------------------------------------------------
# Environment variables:
#------------------------------------------------------------------------------

ENV NODE_EXPORTER_VERSION="0.13.0" \
    HAPROXY_EXPORTER_VERSION="0.7.1" \
    ZK_EXPORTER_VERSION="0.0.1" \
    MESOS_EXPORTER_VERSION="1.0-rc1"

ENV NODE_EXPORTER_URL="https://github.com/prometheus/node_exporter/releases/download/v${NODE_EXPORTER_VERSION}/node_exporter-${NODE_EXPORTER_VERSION}.linux-amd64.tar.gz" \
    HAPROXY_EXPORTER_URL="https://github.com/prometheus/haproxy_exporter/releases/download/v${HAPROXY_EXPORTER_VERSION}/haproxy_exporter-${HAPROXY_EXPORTER_VERSION}.linux-amd64.tar.gz" \
    ZK_EXPORTER_URL="https://github.com/discordianfish/zookeeper_exporter/releases/download/${ZK_EXPORTER_VERSION}/zookeeper_exporter-v${ZK_EXPORTER_VERSION}-amd64-linux.gz" \
    MESOS_EXPORTER_URL="https://github.com/mesosphere/mesos_exporter/releases/download/v${MESOS_EXPORTER_VERSION}/mesos-exporter-v${MESOS_EXPORTER_VERSION}-amd64-linux.gz"

#------------------------------------------------------------------------------
# Install:
#------------------------------------------------------------------------------

RUN apk --no-cache add --update -t deps openssl; cd /tmp \
    && wget -O - ${NODE_EXPORTER_URL} | tar zxvf -; mv node_*/*_exporter /bin/ \
    && wget -O - ${HAPROXY_EXPORTER_URL} | tar zxvf -; mv haproxy_*/*_exporter /bin/ \
    && wget -O - ${ZK_EXPORTER_URL} | zcat > /bin/zookeeper_exporter \
    && wget -O - ${MESOS_EXPORTER_URL} | zcat > /bin/mesos_exporter \
    && chmod +x /bin/*_exporter; apk del --purge deps; rm -rf /tmp/* /var/cache/apk/*

#------------------------------------------------------------------------------
# Expose ports:
#------------------------------------------------------------------------------

EXPOSE 9101 9102 9103 9104
