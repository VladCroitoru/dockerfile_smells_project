# VERSION 1.0
# AUTHOR: Matthieu "Puckel_" Roisil
# DESCRIPTION: Basic InfluxDB container
# BUILD: docker build --rm -t puckel/docker-influxdb
# SOURCE: https://github.com/puckel/docker-influxdb

FROM puckel/docker-base
MAINTAINER Puckel_

# Never prompts the user for choices on installation/configuration of packages
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux
# Work around initramfs-tools running on kernel 'upgrade': <http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=594189>
ENV INITRD No
ENV PRE_CREATE_DB collectd

RUN apt-get update -yqq \
    && apt-get install -yqq ca-certificates \
    && curl -s -O https://s3.amazonaws.com/influxdb/influxdb_latest_amd64.deb \
    && dpkg -i influxdb_latest_amd64.deb \
    && rm influxdb_latest_amd64.deb
ADD config/config.toml /opt/influxdb/shared/config.toml
ADD https://raw.githubusercontent.com/collectd/collectd/master/src/types.db /usr/share/collectd/types.db
ADD scripts/run.sh /run.sh
RUN chmod +x /run.sh


EXPOSE 8083 8086 8090 8099 25826/udp

ENTRYPOINT ["/run.sh"]
