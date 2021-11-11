FROM alpine:latest

MAINTAINER Viktor Sokolov <gzigzigzeo@evilmartians.com>

LABEL maintainer="Viktor Sokolov <gzigzigzeo@evilmartians.com>" \
      org.label-schema.build-date="${BUILD_DATE}" \
      org.label-schema.vcs-ref="${VCS_REF}" \
      org.label-schema.vcs-url="https://github.com/gzigzigzeo/docker-download-confd"

RUN apk add --no-cache curl ca-certificates

ONBUILD ARG CONFD_VERSION
ONBUILD RUN curl -f -L -o /usr/local/bin/confd https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-amd64 && chmod +x /usr/local/bin/confd
