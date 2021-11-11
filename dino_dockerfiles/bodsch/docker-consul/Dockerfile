
FROM golang:1-alpine as builder

ARG VCS_REF
ARG BUILD_DATE
ARG BUILD_VERSION
ARG BUILD_TYPE
ARG CONSUL_VERSION

ENV \
  TERM=xterm \
  GOPATH=/opt/go \
  GOOS=linux \
  GOARCH=amd64 \
  GOMAXPROCS=4

# ---------------------------------------------------------------------------------------

RUN \
  echo "export BUILD_DATE=${BUILD_DATE}"           > /etc/profile.d/consul.sh && \
  echo "export BUILD_TYPE=${BUILD_TYPE}"          >> /etc/profile.d/consul.sh && \
  echo "export CONSUL_VERSION=${CONSUL_VERSION}"  >> /etc/profile.d/consul.sh

# hadolint ignore=DL3017,DL3018
RUN \
  apk update  --quiet --no-cache && \
  apk upgrade --quiet --no-cache && \
  apk add     --quiet --no-cache \
    bash git ncurses make zip

WORKDIR /opt/go

RUN \
  mkdir -p src/github.com/hashicorp

WORKDIR /opt/go/src/github.com/hashicorp

RUN \
  git clone https://github.com/hashicorp/consul.git

WORKDIR /opt/go/src/github.com/hashicorp/consul

RUN \
  if [ "${BUILD_TYPE}" = "stable" ] ; then \
    echo "switch to stable Tag v${CONSUL_VERSION}" && \
    git checkout "tags/v${CONSUL_VERSION}" 2> /dev/null ; \
  fi

# hadolint ignore=DL4006,SC2153
RUN \
  CONSUL_VERSION=$(git describe --tags --always | sed 's/^v//') && \
  echo " => build version ${CONSUL_VERSION}"

RUN \
  export PATH="${GOPATH}/bin:${PATH}" && \
  make linux

RUN \
  mkdir /etc/consul.d && \
  cp -a   bin/consul /usr/bin/ && \
  cp -ar  bench/conf/*.json  /etc/consul.d/

# ---------------------------------------------------------------------------------------

FROM alpine:3.10

# https://www.consul.io/docs/agent/options.html#ports
# Server RPC address
EXPOSE 8300
# The Serf LAN port
EXPOSE 8301 8301/udp
# The Serf WAN port
EXPOSE 8302 8302/udp
# The HTTP API
EXPOSE 8500
# The HTTPS API
EXPOSE 8501
# The gRPC API
EXPOSE 8502
# The DNS server
EXPOSE 8600 8600/udp

COPY --from=builder /etc/profile.d/consul.sh  /etc/profile.d/consul.sh
COPY --from=builder /usr/bin/consul           /usr/bin/consul
COPY --from=builder /etc/consul.d             /etc/consul.d

# hadolint ignore=DL3017,DL3018
RUN \
  apk update  --quiet --no-cache && \
  apk upgrade --quiet --no-cache && \
  apk add     --quiet --no-cache \
    curl && \
  rm -rf \
    /src \
    /tmp/* \
    /root/.cache \
    /var/cache/apk/*

VOLUME ["/data"]

ENTRYPOINT ["/usr/bin/consul"]

HEALTHCHECK \
  --interval=5s \
  --timeout=2s \
  --retries=12 \
  CMD curl --silent --fail localhost:8500 || exit 1

CMD ["agent", "-data-dir", "/data"]

# ---------------------------------------------------------------------------------------

LABEL \
  version="${BUILD_VERSION}" \
  maintainer="Bodo Schulz <bodo@boone-schulz.de>" \
  org.label-schema.build-date=${BUILD_DATE} \
  org.label-schema.name="Consul Docker Image" \
  org.label-schema.description="Inofficial Consul Docker Image" \
  org.label-schema.url="https://www.consul.io/" \
  org.label-schema.vcs-url="https://github.com/bodsch/docker-consul" \
  org.label-schema.vcs-ref=${VCS_REF} \
  org.label-schema.vendor="Bodo Schulz" \
  org.label-schema.version=${CONSUL_VERSION} \
  org.label-schema.schema-version="1.0" \
  com.microscaling.docker.dockerfile="/Dockerfile" \
  com.microscaling.license="GNU Lesser General Public License v2.1"

# ---------------------------------------------------------------------------------------
