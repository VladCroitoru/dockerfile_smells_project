
FROM golang:1-alpine as builder

ARG VCS_REF
ARG BUILD_DATE
ARG BUILD_VERSION
ARG BUILD_TYPE
ARG VAULT_VERSION

ENV \
  TERM=xterm \
  GOPATH=/opt/go \
  GOMAXPROCS=4 \
  GOOS=linux

# ---------------------------------------------------------------------------------------

RUN \
  echo "export BUILD_DATE=${BUILD_DATE}"         > /etc/profile.d/vault.sh && \
  echo "export BUILD_TYPE=${BUILD_TYPE}"        >> /etc/profile.d/vault.sh && \
  echo "export VAULT_VERSION=${VAULT_VERSION}"  >> /etc/profile.d/vault.sh

# hadolint ignore=DL3017,DL3018
RUN \
  apk update  --quiet --no-cache && \
  apk upgrade --quiet --no-cache && \
  apk add     --quiet --no-cache \
    bash git make ncurses zip

WORKDIR /tmp

RUN \
  go get github.com/hashicorp/vault || true

WORKDIR /opt/go/src/github.com/hashicorp/vault

RUN \
  if [ "${BUILD_TYPE}" == "stable" ] ; then \
    echo "switch to stable Tag v${VAULT_VERSION}" && \
    git checkout "tags/v${VAULT_VERSION}" 2> /dev/null ; \
  fi

RUN \
  export PATH="${GOPATH}/bin:${PATH}" && \
  make bootstrap && \
  make && \
  cp bin/vault /usr/bin/

# ---------------------------------------------------------------------------------------

FROM alpine:3.9

EXPOSE 8200

COPY --from=builder /etc/profile.d/vault.sh  /etc/profile.d/vault.sh
COPY --from=builder /usr/bin/vault           /usr/bin/vault

ENTRYPOINT ["/usr/bin/vault"]

CMD ["version"]

HEALTHCHECK \
  --interval=5s \
  --timeout=2s \
  --retries=12 \
  --start-period=10s \
  CMD ps ax -o pid,args | pgrep -v grep | pgrep vault || exit 1

# ---------------------------------------------------------------------------------------

LABEL \
  version="${BUILD_VERSION}" \
  maintainer="Bodo Schulz <bodo@boone-schulz.de>" \
  org.label-schema.build-date=${BUILD_DATE} \
  org.label-schema.name="Vault Docker Image" \
  org.label-schema.description="Inofficial Vault Docker Image" \
  org.label-schema.url="https://www.vaultproject.io/" \
  org.label-schema.vcs-url="https://github.com/bodsch/docker-vault" \
  org.label-schema.vcs-ref=${VCS_REF} \
  org.label-schema.vendor="Bodo Schulz" \
  org.label-schema.version=${VAULT_VERSION} \
  org.label-schema.schema-version="1.0" \
  com.microscaling.docker.dockerfile="/Dockerfile" \
  com.microscaling.license="GNU Lesser General Public License v2.1"

# ---------------------------------------------------------------------------------------
