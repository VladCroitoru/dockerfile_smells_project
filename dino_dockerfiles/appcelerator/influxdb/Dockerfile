FROM appcelerator/alpine:3.5.1
MAINTAINER Nicolas Degory <ndegory@axway.com>

ENV INFLUXDB_VERSION 1.2.0

RUN apk update && apk upgrade && \
    apk --virtual build-deps add go curl python git gcc musl-dev make patch && \
    export GOPATH=/go && \
    go get -v github.com/influxdata/influxdb && \
    cd $GOPATH/src/github.com/influxdata/influxdb && \
    git checkout -q --detach "v${INFLUXDB_VERSION}" && \
    python ./build.py && \
    chmod +x ./build/influx* && \
    mv ./build/influx* /bin/ && \
    mkdir -p /etc/influxdb /data/influxdb /data/influxdb/meta /data/influxdb/data /var/tmp/influxdb/wal /var/log/influxdb && \
    apk del build-deps && cd / && rm -rf $GOPATH/ /var/cache/apk/*

RUN apk update && apk add util-linux && rm -rf /var/cache/apk/*

ENV ADMIN_USER root
ENV INFLUXDB_INIT_PWD root

ADD types.db /usr/share/collectd/types.db
ADD config.toml /etc/influxdb/config.toml.tpl
ADD run.sh /run.sh

ENV PRE_CREATE_DB **None**

# Admin server WebUI
EXPOSE 8083
# HTTP API
EXPOSE 8086

VOLUME ["/data"]

ENTRYPOINT ["/bin/sh", "-c"]
CMD ["/run.sh"]

HEALTHCHECK --interval=5s --retries=24 --timeout=1s CMD curl -sI 127.0.0.1:8086/ping | grep -q "204 No Content"
