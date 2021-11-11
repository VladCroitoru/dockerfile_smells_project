FROM golang:1-alpine as builder

ARG BUILD_DATE
ARG BUILD_VERSION
ARG BUILD_TYPE
ARG VERSION

ENV TERM=xterm
ENV GOPATH=/opt/go
ENV CGO_ENABLED=0
ENV GO111MODULE=on
ENV PATH="${PATH}:${GOPATH}/bin"

# ---------------------------------------------------------------------------------------

SHELL ["/bin/sh", "-o", "pipefail", "-c"]

# hadolint ignore=DL3017,DL3018
RUN \
  apk update  --quiet --no-cache && \
  apk upgrade --quiet --no-cache && \
  apk add     --quiet --no-cache \
    g++ \
    git \
    make \
    musl-dev

# hadolint ignore=DL3059
RUN \
  echo "export BUILD_DATE=${BUILD_DATE}"  > /etc/profile.d/carbon-relay-ng.sh && \
  echo "export BUILD_TYPE=${BUILD_TYPE}" >> /etc/profile.d/carbon-relay-ng.sh && \
  echo "export VERSION=${VERSION}"       >> /etc/profile.d/carbon-relay-ng.sh

WORKDIR ${GOPATH}

# hadolint ignore=DL3059
RUN \
  git clone https://github.com/grafana/carbon-relay-ng.git
# hadolint ignore=DL3059
RUN \
  go get github.com/shuLhan/go-bindata/cmd/go-bindata

WORKDIR ${GOPATH}/carbon-relay-ng

# hadolint ignore=DL4006,DL3059,SC2153
RUN \
  if [ "${BUILD_TYPE}" = "stable" ] ; then \
    echo "switch to stable Tag v${VERSION}" && \
    git checkout "tags/v${VERSION}" 2> /dev/null ; \
  fi && \
  version=$(git describe --tags --always | sed 's/^v//') && \
  echo "build version: ${version}"
# hadolint ignore=DL3059
RUN \
  export PATH="${PATH}:${GOPATH}/bin" && \
  make
# hadolint ignore=DL3059
RUN \
  mv -v carbon-relay-ng /tmp/carbon-relay-ng && \
  mv -v examples /tmp/

# ---------------------------------------------------------------------------------------

FROM alpine:3

ARG VCS_REF
ARG BUILD_DATE
ARG BUILD_VERSION
ARG BUILD_TYPE
ARG VERSION

ENV \
  TERM=xterm \
  TZ='Europe/Berlin'

# ---------------------------------------------------------------------------------------

COPY --from=builder /etc/profile.d/carbon-relay-ng.sh  /etc/profile.d/carbon-relay-ng.sh
COPY --from=builder /tmp/carbon-relay-ng               /usr/bin/carbon-relay-ng
COPY --from=builder /tmp/examples/storage-schemas.conf /etc/carbon-relay-ng/storage-schemas.conf-DIST
COPY --from=builder /tmp/examples/carbon-relay-ng.ini  /etc/carbon-relay-ng/carbon-relay-ng.ini-DIST
COPY rootfs/ /

# hadolint ignore=DL3017,DL3018
RUN \
  apk update  --quiet --no-cache && \
  apk upgrade --quiet --no-cache && \
  apk add     --quiet --no-cache \
    bash netcat-openbsd && \
  apk add     --quiet --no-cache --virtual .build-deps \
    shadow \
    tzdata && \
  cp "/usr/share/zoneinfo/${TZ}" /etc/localtime && \
  echo "${TZ}" > /etc/timezone && \
  /usr/sbin/useradd \
    --system \
    --user-group \
    --shell /bin/false \
    --home-dir /home/relay \
    --comment "User for Graphite daemon" \
    relay && \
  mkdir /home/relay && \
  mkdir /var/spool/carbon-relay-ng && \
  chown -R relay:relay \
    /home/relay \
    /etc/carbon-relay-ng.ini* \
    /etc/carbon-relay-ng \
    /var/spool/carbon-relay-ng && \
  chgrp relay /var/spool && \
  chmod g+w /var/spool && \
  apk --quiet --purge del .build-deps && \
  rm -rf \
    /tmp/* \
    /var/cache/apk/*

WORKDIR /home/relay
# VOLUME ["/home/relay" "/etc/carbon-relay-ng"]
USER relay

HEALTHCHECK \
  --interval=5s \
  --timeout=2s \
  --retries=12 \
  --start-period=10s \
  CMD ps ax | grep -v grep | grep -c "/usr/bin/carbon-relay-ng" || exit 1

CMD ["/init/run.sh"]

# ---------------------------------------------------------------------------------------

EXPOSE 2003 2004 8081

LABEL \
  version=${BUILD_VERSION} \
  maintainer="Bodo Schulz <bodo@boone-schulz.de>" \
  org.label-schema.build-date=${BUILD_DATE} \
  org.label-schema.name="carbon-relay-ng Docker Image" \
  org.label-schema.description="Inofficial carbon-relay-ng Docker Image" \
  org.label-schema.url="https://github.com/grafana/carbon-relay-ng" \
  org.label-schema.vcs-ref=${VCS_REF} \
  org.label-schema.vcs-url="https://github.com/bodsch/docker-docker-carbon-relay-ng" \
  org.label-schema.vendor="Bodo Schulz" \
  org.label-schema.version=${VERSION} \
  org.label-schema.schema-version="1.0" \
  com.microscaling.docker.dockerfile="/Dockerfile" \
  com.microscaling.license="The Unlicense"

# EOF
