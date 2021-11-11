FROM golang:1.11.2-alpine3.8
LABEL maintainer "terje@offpiste.org"

ENV INFLUXDB_URL=http://influxdb:8086/
ENV INFLUXDB_DATABASE=prometheus
ENV INFLUXDB_RETENTION_POLICY=autogen
ENV INFLUXDB_USER=influx
ENV INFLUXDB_PW=influx

EXPOSE 9201

COPY run.sh /

RUN apk add --no-cache git && \
    mkdir -p /go/src/github.com/prometheus && \
    cd /go/src/github.com/prometheus && \
    git clone --branch v2.5.0 --depth 1 https://github.com/prometheus/prometheus.git && \
    go get -d -v /go/src/github.com/prometheus/prometheus/documentation/examples/remote_storage/remote_storage_adapter && \
    go install -v /go/src/github.com/prometheus/prometheus/documentation/examples/remote_storage/remote_storage_adapter && \
    cd / && \
    apk del git && \
    rm -rf /go/src/github.com /var/cache/apk

CMD ["/run.sh"]
