
FROM golang:1-alpine as builder

ARG BUILD_DATE
ARG BUILD_VERSION

# ---------------------------------------------------------------------------------------

WORKDIR /opt/go

RUN \
  apk update --no-cache && \
  apk upgrade --no-cache && \
  apk add \
    ca-certificates curl g++ git make python libuv nodejs nodejs-npm && \
  echo "export BUILD_DATE=${BUILD_DATE}" > /etc/enviroment

RUN \
  export GOPATH=/opt/go && \
  go get github.com/aerth/markdownd || true && \
  mkdir /tmp/markdownd && \
  export GOPATH=/opt/go && \
  export GOMAXPROCS=4 && \
  export GOARCH=amd64 && \
  cd ${GOPATH}/src/github.com/aerth/markdownd && \
  version=$(git describe --tags --always | sed 's/^v//') && \
  echo "build version: ${version}" && \
  ls -1 && \
  /bin/sh ./build.sh && \
  mv markdownd /tmp/markdownd/ && \
  mv theme /tmp/markdownd/

CMD [ "/bin/sh" ]

# ---------------------------------------------------------------------------------------

FROM alpine:3.8

EXPOSE 8080

COPY --from=builder /etc/enviroment /etc/enviroment
COPY --from=builder /tmp/markdownd/ /markdownd

RUN \
  export TZ='Europe/Berlin' && \
  apk update --quiet --no-cache update && \
  apk add --quiet --no-cache --virtual .build-deps \
    tzdata && \
  cp /usr/share/zoneinfo/${TZ} /etc/localtime && \
  echo ${TZ} > /etc/timezone && \
  if [ -f /etc/enviroment ] ; then . /etc/enviroment; fi && \
  apk del --quiet .build-deps && \
  rm -rf \
    /tmp/* \
    /var/cache/apk/*

VOLUME [ "/markdownd", "/data" ]

WORKDIR /markdownd

ENTRYPOINT [ "/markdownd/markdownd" ]

CMD [ "-toc", "-footer", "/data/themes/footer.html", "-header", "/data/themes/header.html", "-index", "index.md", "/data" ]

# ---------------------------------------------------------------------------------------

LABEL \
  version="${BUILD_VERSION}" \
  maintainer="Bodo Schulz <bodo@boone-schulz.de>" \
  org.label-schema.build-date=${BUILD_DATE} \
  org.label-schema.name="markdownd Docker Image" \
  org.label-schema.description="Inofficial markdownd Docker Image" \
  org.label-schema.url="https://markdownd.herokuapp.com/" \
  org.label-schema.vcs-url="https://github.com/bodsch/docker-markdownd" \
  org.label-schema.vendor="Bodo Schulz" \
  org.label-schema.schema-version="1.0" \
  com.microscaling.docker.dockerfile="/Dockerfile" \
  com.microscaling.license="MIT License"

# ---------------------------------------------------------------------------------------
