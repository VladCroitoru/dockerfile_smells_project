ARG GRAFANA_VERSION
# use the official container as base
FROM grafana/grafana:${GRAFANA_VERSION}

ARG VCS_REF
ARG BUILD_DATE
ARG BUILD_VERSION
ARG BUILD_TYPE=stable
ARG GRAFANA_VERSION

ENV \
  TERM=xterm-256color \
  DEBIAN_FRONTEND=noninteractive \
  TZ='Europe/Berlin'

# hadolint ignore=DL3002
USER root

# hadolint ignore=SC1091,DL3008,DL3014,DL3015,DL4005,DL4006
RUN \
  chsh -s /bin/bash && \
  ln -sf /bin/bash /bin/sh && \
  ln -sf "/usr/share/zoneinfo/${TZ}" /etc/localtime && \
  echo "${TZ}" > /etc/timezone && \
  apt-get update && \
  echo "export BUILD_DATE=${BUILD_DATE}"           >  /etc/profile.d/grafana.sh && \
  echo "export BUILD_TYPE=${BUILD_TYPE}"           >> /etc/profile.d/grafana.sh && \
  echo "export GRAFANA_VERSION=${GRAFANA_VERSION}" >> /etc/profile.d/grafana.sh && \
  [ -d /home/grafana ] || mkdir /home/grafana && \
  chown grafana:grafana /home/grafana && \
  [ -f /etc/profile.d/grafana.sh ] && . /etc/profile && \
  cp /etc/grafana/grafana.ini /home/grafana/grafana.ini-DIST && \
  apt-get install --no-install-recommends --assume-yes \
    ca-certificates \
    curl \
    jq \
    less \
    mariadb-client \
    nano \
    net-tools \
    netcat-openbsd \
    pwgen \
    procps \
    sqlite \
    yajl-tools \
    libfontconfig1 \
    && \
    # install my favorite grafana plugins
    echo "install my favorite grafana plugins ..." && \
    for plugin in \
      blackmirror1-statusbygroup-panel \
      btplc-trend-box-panel \
      digiapulssi-breadcrumb-panel \
      grafana-clock-panel \
      grafana-piechart-panel \
      jdbranham-diagram-panel \
      michaeldmoore-annunciator-panel \
      mtanda-histogram-panel \
      natel-discrete-panel \
      neocat-cal-heatmap-panel \
      vonage-status-panel \
      petrslavotinek-carpetplot-panel \
      snuids-radar-panel \
      zuburqan-parity-report-panel ; \
    do \
       /usr/share/grafana/bin/grafana-cli \
        --pluginsDir "/var/lib/grafana/plugins" \
        plugins \
        install ${plugin} ; \
    done && \
  apt-get clean && \
  apt autoremove --assume-yes && \
  rm -rf \
    /tmp/* \
    /var/cache/debconf/* \
    /usr/share/doc/* \
    /root/.gem \
    /root/.cache \
    /root/.bundle 2> /dev/null

COPY rootfs/ /

VOLUME ["/usr/share/grafana/data", "/usr/share/grafana/public/dashboards", "/opt/grafana/dashboards","/etc/grafana/provisioning"]

USER grafana

ENTRYPOINT ["/init/run.sh"]

HEALTHCHECK \
  --interval=5s \
  --timeout=2s \
  --retries=12 \
  CMD curl --silent --fail localhost:3000 || exit 1

# ---------------------------------------------------------------------------------------

LABEL \
  version=${BUILD_VERSION} \
  maintainer="Bodo Schulz <bodo@boone-schulz.de>" \
  org.label-schema.build-date=${BUILD_DATE} \
  org.label-schema.name="Grafana Docker Image" \
  org.label-schema.description="Inofficial Grafana Docker Image" \
  org.label-schema.url="https://www.grafana.com" \
  org.label-schema.vcs-url="https://github.com/bodsch/docker-grafana" \
  org.label-schema.vcs-ref=${VCS_REF} \
  org.label-schema.vendor="Bodo Schulz" \
  org.label-schema.version=${GRAFANA_VERSION} \
  org.label-schema.schema-version="1.0" \
  com.microscaling.docker.dockerfile="/Dockerfile" \
  com.microscaling.license="GNU Lesser General Public License v3.0"

# ---------------------------------------------------------------------------------------
