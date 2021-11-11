FROM alpine:latest
MAINTAINER Janez Troha <dz0ny@ubuntu.si>

# Install InfluxDB
ENV INFLUXDB_VERSION static-nightly

RUN apk add --update wget tar ca-certificates && rm -rf /var/cache/apk/*
RUN wget https://s3.amazonaws.com/influxdb/influxdb-${INFLUXDB_VERSION}_linux_amd64.tar.gz
RUN mkdir -p /app /var/lib/influxdb/ && \
    tar xfz influxdb-${INFLUXDB_VERSION}_linux_amd64.tar.gz -C /app && \
	rm influxdb-${INFLUXDB_VERSION}_linux_amd64.tar.gz

# Admin server WebUI
EXPOSE 8083

# HTTP API
EXPOSE 8086

VOLUME ["/var/lib/influxdb"]

ENTRYPOINT ["/app/influxd"]
CMD ["run", "-config", "/app/influxdb.conf"]