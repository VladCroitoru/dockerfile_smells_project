ARG DOCKER_REGISTRY=docker.io
ARG FROM_IMG=qnib/alplain-openjre8-glibc
FROM ${DOCKER_REGISTRY}/${FROM_IMG}

ARG GRAFANA_VER=4.6.3
LABEL grafana.version=${GRAFANA_VER}
ENV GRAFANA_DATA_SOURCES=prometheus,influxdb \
    GF_PLUGIN_DIR=/opt/grafana/plugins/ \
    INFLUXDB_HOST=tasks.influxdb \
    INFLUXDB_DB=none \
    PROMETHEUS_PORT=9090 \
    PROMETHEUS_HOST=tasks.prometheus \
    ENTRYPOINTS_DIR=/opt/qnib/entry

RUN apk --no-cache add sqlite openssl curl rsync nmap \
 && wget -qO - https://s3-us-west-2.amazonaws.com/grafana-releases/release/grafana-${GRAFANA_VER}.linux-x64.tar.gz |tar xfz - -C /opt/ \
 && mv /opt/grafana-${GRAFANA_VER} /opt/grafana
COPY etc/grafana/grafana.ini /etc/grafana/grafana.ini
COPY opt/qnib/grafana/bin/healthcheck.sh \
     opt/qnib/grafana/bin/backup_dash.sh \
     /opt/qnib/grafana/bin/
## Apps
RUN /opt/grafana/bin/grafana-cli plugins install bosun-app
## Datasources
RUN /opt/grafana/bin/grafana-cli plugins install crate-datasource
RUN /opt/grafana/bin/grafana-cli plugins install grafana-kairosdb-datasource
RUN /opt/grafana/bin/grafana-cli plugins install grafana-simple-json-datasource
RUN /opt/grafana/bin/grafana-cli plugins install hawkular-datasource
RUN /opt/grafana/bin/grafana-cli plugins install opennms-datasource
## Panels
RUN /opt/grafana/bin/grafana-cli plugins install briangann-gauge-panel
RUN /opt/grafana/bin/grafana-cli plugins install digiapulssi-breadcrumb-panel
RUN /opt/grafana/bin/grafana-cli plugins install digiapulssi-organisations-panel
RUN /opt/grafana/bin/grafana-cli plugins install grafana-worldmap-panel
RUN /opt/grafana/bin/grafana-cli plugins install jdbranham-diagram-panel
RUN /opt/grafana/bin/grafana-cli plugins install natel-discrete-panel
RUN /opt/grafana/bin/grafana-cli plugins install natel-influx-admin-panel
RUN /opt/grafana/bin/grafana-cli plugins install neocat-cal-heatmap-panel
RUN /opt/grafana/bin/grafana-cli plugins install savantly-heatmap-panel
RUN /opt/grafana/bin/grafana-cli plugins install vonage-status-panel

COPY opt/qnib/env/grafana/api_key.sh /opt/qnib/env/grafana/
COPY opt/qnib/grafana/sql/api_keys/viewer.sql /opt/qnib/grafana/sql/api_keys/
COPY opt/qnib/entry/20-grafana-sql-restore.sh \
     opt/qnib/entry/15-grafana-sql-bootstrap.sh \
     opt/qnib/entry/10-grafana-plugins-dir.sh \
     /opt/qnib/entry/
## SQL dumps to setup /var/lib/grafana/grafana.db
COPY opt/qnib/grafana/sql/00-migration_log.sql \
     opt/qnib/grafana/sql/10-user.sql \
     opt/qnib/grafana/sql/20-init-dash.sql \
     opt/qnib/grafana/sql/30-data-source.sql \
     opt/qnib/grafana/sql/40-backend.sql \
     /opt/qnib/grafana/sql/
COPY opt/qnib/grafana/sql/data-sources/*.sql \
     /opt/qnib/grafana/sql/data-sources/
COPY opt/qnib/grafana/sql/dashboards/*.sql \
     /opt/qnib/grafana/sql/dashboards/
VOLUME ["/opt/grafana/sql/"]
HEALTHCHECK --interval=5s --retries=15 --timeout=1s \
  CMD /opt/qnib/grafana/bin/healthcheck.sh
CMD ["/opt/grafana/bin/grafana-server", \
     "-homepath=/opt/grafana/", \
     "--pidfile=/var/run/grafana-server.pid", \
     "--config=/etc/grafana/grafana.ini", \
     "cfg:default.paths.data=/var/lib/grafana", \
     "cfg:default.paths.logs=/var/log/grafana"]
