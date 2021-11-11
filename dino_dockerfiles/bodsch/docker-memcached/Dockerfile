
FROM alpine:3.7
#FROM memcached:1.5.4-alpine

MAINTAINER Bodo Schulz <bodo@boone-schulz.de>

ENV \
  TERM=xterm \
  BUILD_DATE="2017-12-08" \
  VERSION="1.5.3"

EXPOSE 11211

LABEL \
  version="1712" \
  org.label-schema.build-date=${BUILD_DATE} \
  org.label-schema.name="Memcached Docker Image" \
  org.label-schema.description="Inofficial Memcached Docker Image" \
  org.label-schema.url="http://memcached.org" \
  org.label-schema.vcs-url="https://github.com/bodsch/docker-memcached" \
  org.label-schema.vendor="Bodo Schulz" \
  org.label-schema.version=${VERSION} \
  org.label-schema.schema-version="1.0" \
  com.microscaling.docker.dockerfile="/Dockerfile" \
  com.microscaling.license="The Unlicense"

# ---------------------------------------------------------------------------------------

RUN \
  apk update --no-cache && \
  apk upgrade --no-cache && \
  apk add --quiet \
    memcached && \
  adduser -D memcache && \
  rm -rf \
    /tmp/* \
    /var/cache/apk/*

HEALTHCHECK \
  --interval=5s \
  --timeout=2s \
  --retries=12 \
  CMD /bin/echo stats | nc 127.0.0.1 11211 | grep -c version || exit 1


ENTRYPOINT [ "/usr/bin/memcached" ]

CMD [ "-l", "0.0.0.0", "-m", "8", "-u", "memcached" ]

# EOF
