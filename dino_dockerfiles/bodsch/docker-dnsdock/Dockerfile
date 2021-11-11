
FROM alpine:3.6

MAINTAINER Bodo Schulz <bodo@boone-schulz.de>

ENV \
  ALPINE_MIRROR="mirror1.hs-esslingen.de/pub/Mirrors" \
  ALPINE_VERSION="v3.6" \
  TERM=xterm \
  BUILD_DATE="2017-08-29" \
  VERSION="1.16.4" \
  GOPATH=/opt/go

EXPOSE 53 53/udp 80

LABEL \
  version="1708-35" \
  org.label-schema.build-date=${BUILD_DATE} \
  org.label-schema.name="dnsdock Docker Image" \
  org.label-schema.description="Inofficial dnsdock Docker Image" \
  org.label-schema.url="https://github.com/aacebedo/dnsdock" \
  org.label-schema.vcs-url="https://github.com/bodsch/docker-dnsdock" \
  org.label-schema.vendor="Bodo Schulz" \
  org.label-schema.version=${DNSDOCK_VERSION} \
  org.label-schema.schema-version="1.0" \
  com.microscaling.docker.dockerfile="/Dockerfile" \
  com.microscaling.license="GNU General Public License v3.0"

# ---------------------------------------------------------------------------------------

RUN \
  echo "http://${ALPINE_MIRROR}/alpine/${ALPINE_VERSION}/main"       > /etc/apk/repositories && \
  echo "http://${ALPINE_MIRROR}/alpine/${ALPINE_VERSION}/community" >> /etc/apk/repositories && \
  echo "http://${ALPINE_MIRROR}/alpine/edge/community"              >> /etc/apk/repositories && \
  apk --no-cache update && \
  apk --no-cache upgrade && \
  apk --no-cache add \
    drill \
    g++ \
    git \
    go \
    make && \
  mkdir -p ${GOPATH} && \
  export PATH="${PATH}:${GOPATH}/bin" && \
  go get github.com/tools/godep && \
  go get github.com/aacebedo/dnsdock || true && \
  cd ${GOPATH}/src/github.com/aacebedo/dnsdock && \
  godep restore && \
  cd ${GOPATH}/src/github.com/aacebedo/dnsdock/src && \
  git describe --contains HEAD && \
  go build -o /usr/bin/dnsdock && \
  apk del --purge \
    build-base \
    git \
    go && \
  rm -rf \
    ${GOPATH} \
    /usr/lib/go \
    /usr/bin/go \
    /usr/bin/gofmt \
    /tmp/* \
    /var/cache/apk/*

WORKDIR /

ENTRYPOINT [ "/usr/bin/dnsdock" ]

# ---------------------------------------------------------------------------------------
