FROM tutum/curl:trusty
MAINTAINER Timo Boll

# Install InfluxDB
ENV INFLUXDB_HOME /influxdb
ENV INFLUXDB_VERSION 0.8.8
COPY ${INFLUXDB_VERSION}/influxdb_${INFLUXDB_VERSION}_amd64.deb /tmp/influxdb_latest_amd64.deb
RUN dpkg -i /tmp/influxdb_latest_amd64.deb && \
  rm /tmp/influxdb_latest_amd64.deb

ADD config.toml /config/config.toml
ADD run.sh /run.sh
RUN chmod +x /*.sh

ENV PRE_CREATE_DB "grafana;gatling"
ENV SSL_SUPPORT **False**
ENV SSL_CERT **None**

# Admin server
EXPOSE 8083

# HTTP API
EXPOSE 8086

# HTTPS API
EXPOSE 8084

# HTTPS API
EXPOSE 2003

# Raft port (for clustering, don't expose publicly!)
#EXPOSE 8090

# Protobuf port (for clustering, don't expose publicly!)
#EXPOSE 8099

VOLUME ["/data"]

CMD ["/run.sh"]
