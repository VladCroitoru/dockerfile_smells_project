FROM telegraf:alpine

COPY telegraf.conf /etc/telegraf/telegraf.conf

ENV INFLUXDB_HOST localhost
ENV INFLUXDB_DATABASE db0
ENV INFLUXDB_PORT 8086
ENV STATSD_PROTOCOL udp
