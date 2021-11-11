FROM debian:jessie
MAINTAINER Ben Bailey <bennettbailey@gmail.com>

ENV TELEGRAF_VERSION 0.2.4
RUN apt-get update && \
  apt-get install -y curl && \
  curl -s -o /tmp/telegraf_latest_amd64.deb http://get.influxdb.org/telegraf/telegraf_${TELEGRAF_VERSION}_amd64.deb && \
  dpkg -i /tmp/telegraf_latest_amd64.deb && \
  rm /tmp/telegraf_latest_amd64.deb && \
  rm -rf /var/lib/apt/lists/*

COPY telegraf.toml /config/telegraf.toml
COPY run.sh /run.sh
RUN chmod +x /run.sh

ENV INFLUXDB_HOST **None**

CMD ["/run.sh"]
