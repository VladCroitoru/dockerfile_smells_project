###### QNIBTerminal child
FROM qnib/alplain-golang:1.9.2 AS build

WORKDIR /usr/local/src/github.com/graphite-ng/carbon-relay-ng
RUN apk --no-cache add make \
 && go get -u github.com/jteeuwen/go-bindata/... \
 && wget -qO- https://github.com/graphite-ng/carbon-relay-ng/archive/v0.9.3.tar.gz |tar xfz - --strip-components=1 \
 && make

FROM qnib/alplain-config:2017-11-06.v2
VOLUME ["/var/spool/carbon-relay-ng", "/etc/carbon-relay-ng"]
ENV CARBON_RELAY_LISTEN_PORT=2003 \
    CARBON_RELAY_PICKLE_PORT=2013 \
    CARBON_RELAY_ADMIN_PORT=2004 \
    CARBON_RELAY_ADMIN_BIND_IP=0.0.0.0 \
    CARBON_RELAY_HTTP_PORT=8081 \
    CARBON_RELAY_HTTP_BIND_IP=0.0.0.0 \
    CARBON_RELAY_LOG_LEVEL=notice \
    CARBON_RELAY_INTERNAL_METRICS_TARGET="" \
    CARBON_RELAY_INTERNAL_METRICS_INTERVAL=1000 \
    CARBON_RELAY_MAX_PROCS=2 \
    CARBON_RELAY_VALIDATE_LEVEL_LEGACY=medium \
    CARBON_RELAY_VALIDATE_LEVEL_M20=medium \
    CARBON_RELAY_DESTINATION=tasks.backend:2003
COPY --from=build /usr/local/src/github.com/graphite-ng/carbon-relay-ng/carbon-relay-ng /usr/local/bin/
COPY etc/confd/templates/carbon-relay-ng.conf.tmpl /etc/confd/templates/
COPY etc/confd/conf.d/carbon-relay-ng.toml /etc/confd/conf.d/
CMD ["carbon-relay-ng", "/etc/carbon-relay-ng/carbon-relay-ng.ini"]
