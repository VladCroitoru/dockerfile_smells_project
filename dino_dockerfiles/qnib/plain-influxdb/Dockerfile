FROM qnib/alplain-init

ENV ROOT_PASSWORD=root \
    METRIC_DATABASE=carbon \
    METRIC_USERNAME=carbon \
    METRIC_PASSWORD=carbon \
    DASHBOARD_DATABASE=default \
    DASHBOARD_USERNAME=default \
    DASHBOARD_PASSWORD=default \
    INFLUXDB_META_PORT=8088 \
    INFLUXDB_META_HTTP_PORT=8091 \
    INFLUXDB_ADMIN_HOST=0.0.0.0 \
    INFLUXDB_ADMIN_PORT=8083 \
    INFLUXDB_HTTP_PORT=8086 \
    INFLUXDB_OPENTSDB_PORT=4242 \
    INFLUXDB_GRAPHITE_ENABLED=false \
    INFLUXDB_COLLECTD_ENABLED=false \
    INFLUXDB_OPENTSDB_ENABLED=false \
    INFLUXDB_DATABASES=qcollect \
    INFLUXDB_META_DIR=/opt/influxdb/shared/meta \
    INFLUXDB_META_LOGGING=false \
    INFLUXDB_DATA_DIR=/opt/influxdb/shared/data \
    INFLUXDB_WAL_DIR=/opt/influxdb/shared/wal \
    INFLUXDB_WAL_LOGGING=false \
    INFLUXDB_QUERY_LOGGING=false \
    INFLUXDB_HTTP_LOGGING=false \
    INFLUXDB_TRACE_LOGGING=false \
    ENTRYPOINTS_DIR=/opt/qnib/entry \
    PATH=${PATH}:/opt/influxdb/
ARG INFLUXDB_VER=1.4.3
ARG INFLUXDB_URL=https://dl.influxdata.com/influxdb/releases
ARG CT_VER=0.18.5
RUN apk add --no-cache --virtual .build-deps wget gnupg tar ca-certificates \
 && wget -q https://dl.influxdata.com/influxdb/releases/influxdb-${INFLUXDB_VER}-static_linux_amd64.tar.gz \
 && mkdir -p /usr/src /opt/influxdb/ \
 && tar -C /usr/src -xzf influxdb-${INFLUXDB_VER}-static_linux_amd64.tar.gz \
 && rm -f /usr/src/influxdb-*/influxdb.conf \
 && chmod +x /usr/src/influxdb-*/* \
 && cp -a /usr/src/influxdb-*/* /opt/influxdb/ \
 && rm -rf *.tar.gz* /usr/src /root/.gnupg \
 && apk del .build-deps \
 && apk --no-cache add wget curl \
 && wget -qO /usr/local/bin/go-github https://github.com/qnib/go-github/releases/download/0.2.2/go-github_0.2.2_MuslLinux \
 && chmod +x /usr/local/bin/go-github \
 && echo -n "# Download: " \
 && mkdir -p /usr/share/collectd/ \
 && wget -qO /usr/share/collectd/types.db https://raw.githubusercontent.com/collectd/collectd/master/src/types.db \
 && curl -Lso /tmp/consul-template.zip https://releases.hashicorp.com/consul-template/${CT_VER}/consul-template_${CT_VER}_linux_amd64.zip \
 && cd /usr/local/bin \
 && unzip /tmp/consul-template.zip \
 && apk --no-cache del unzip wget curl \
 && rm -f /tmp/consul-template.zip

COPY opt/qnib/influxdb/bin/start.sh \
   /opt/qnib/influxdb/bin/
COPY opt/healthchecks/20-influxdb.sh /opt/healthchecks/
COPY etc/consul-templates/influxdb/influxdb.conf.ctmpl /etc/consul-templates/influxdb/
COPY opt/qnib/entry/10-influxdb.sh /opt/qnib/entry/
HEALTHCHECK --interval=5s --retries=15 --timeout=1s \
  CMD /usr/local/bin/healthcheck.sh
CMD ["/opt/qnib/influxdb/bin/start.sh"]
