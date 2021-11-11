
FROM alpine:3.7

ENV \
  TERM=xterm \
  BUILD_DATE="2018-01-18" \
  INFLUXDB_VERSION="1.5.0rc0"

EXPOSE 2003 8083 8086

LABEL \
  version="1712" \
  maintainer="Bodo Schulz <bodo@boone-schulz.de>" \
  org.label-schema.build-date=${BUILD_DATE} \
  org.label-schema.name="InfluxDB Docker Image" \
  org.label-schema.description="Inofficial InfluxDB Docker Image" \
  org.label-schema.url="https://github.com/influxdata/influxdb" \
  org.label-schema.vcs-url="https://github.com/bodsch/docker-influxdb" \
  org.label-schema.vendor="Bodo Schulz" \
  org.label-schema.version=${INFLUXDB_VERSION} \
  org.label-schema.schema-version="1.0" \
  com.microscaling.docker.dockerfile="/Dockerfile" \
  com.microscaling.license="GNU General Public License v3.0"

# ---------------------------------------------------------------------------------------

RUN \
  apk update --quiet --no-cache && \
  apk upgrade --quiet --no-cache && \
  echo 'hosts: files dns' >> /etc/nsswitch.conf && \
  apk add --quiet --no-cache \
    tzdata bash jq && \
  set -e && \
  apk add --quiet --no-cache --virtual .build-deps \
    curl gnupg tar ca-certificates && \
  update-ca-certificates 2> /dev/null && \
  for key in \
    05CE15085FC09D18E99EFB22684A14CF2582E0C5 ; \
  do \
    gpg --output /tmp/gpg.out --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" 2> /dev/null || \
    gpg --output /tmp/gpg.out --keyserver pgp.mit.edu --recv-keys "$key" 2> /dev/null || \
    gpg --output /tmp/gpg.out --keyserver keyserver.pgp.com --recv-keys "$key" 2> /dev/null ; \
  done && \
  #
  echo "fetch influxdb ${INFLUXDB_VERSION}" && \
  curl \
    --silent \
    --location \
    --retry 3 \
    --cacert /etc/ssl/certs/ca-certificates.crt \
    --output /tmp/influxdb-${INFLUXDB_VERSION}-static_linux_amd64.tar.gz \
  https://dl.influxdata.com/influxdb/releases/influxdb-${INFLUXDB_VERSION}-static_linux_amd64.tar.gz && \
  #
  curl \
    --silent \
    --location \
    --retry 3 \
    --cacert /etc/ssl/certs/ca-certificates.crt \
    --output /tmp/influxdb-${INFLUXDB_VERSION}-static_linux_amd64.tar.gz.asc \
  https://dl.influxdata.com/influxdb/releases/influxdb-${INFLUXDB_VERSION}-static_linux_amd64.tar.gz.asc && \
  #
  gpg \
    --batch \
    --verify \
    --output /tmp/gpg.out \
    /tmp/influxdb-${INFLUXDB_VERSION}-static_linux_amd64.tar.gz.asc \
    /tmp/influxdb-${INFLUXDB_VERSION}-static_linux_amd64.tar.gz \
    1> /dev/null \
    2> /dev/null && \
  #
  mkdir -p /usr/src && \
  mkdir -p /etc/influxdb && \
  #
  echo "extract archive" && \
  tar -C /usr/src -xzf /tmp/influxdb-${INFLUXDB_VERSION}-static_linux_amd64.tar.gz && \
  #
  cd /usr/src && \
  echo "install files" && \
  find . -name influxdb.conf -print0 | xargs -0 -I{} mv {} /etc/influxdb/influxdb.conf-DIST && \
  if [ ! -d etc ] ; then \
    mv $(ls -1) influxdb ; \
    mv /usr/src/influxdb/influx* /usr/bin/ ; \
  else \
    [ -d usr/bin ] && mv usr/bin/* /usr/bin/ ; \
  fi && \
  chmod -R +x /usr/bin/influx* && \
  #
  apk del .build-deps && \
  rm -rf \
    /tmp/* \
    /usr/src \
    /root/.gnupg \
    /var/cache/apk/*

COPY rootfs/ /

VOLUME [ "/var/lib/influxdb", "/srv" ]

ENTRYPOINT ["/init/run.sh"]

CMD ["influxd"]
