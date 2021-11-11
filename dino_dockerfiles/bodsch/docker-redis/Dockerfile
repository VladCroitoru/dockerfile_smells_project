
FROM alpine:3.7

ENV \
  TERM=xterm \
  BUILD_DATE="2018-01-18" \
  VERSION="3.2.8"

EXPOSE 6379

LABEL \
  version="1801" \
  maintainer="Bodo Schulz <bodo@boone-schulz.de>" \
  org.label-schema.build-date=${BUILD_DATE} \
  org.label-schema.name="redis Docker Image" \
  org.label-schema.description="Inofficial redis Docker Image" \
  org.label-schema.url="https://redis.io/" \
  org.label-schema.vcs-url="https://github.com/bodsch/docker-redis" \
  org.label-schema.vendor="Bodo Schulz" \
  org.label-schema.version=${VERSION} \
  org.label-schema.schema-version="1.0" \
  com.microscaling.docker.dockerfile="/Dockerfile" \
  com.microscaling.license="GNU General Public License v3.0"

# ---------------------------------------------------------------------------------------

RUN \
  apk update --no-cache && \
  apk upgrade --no-cache && \
  apk add --quiet --no-cache \
    redis && \
  mv /etc/redis.conf /etc/redis.conf-DIST && \
  rm -rf \
    /tmp/* \
    /var/cache/apk/*

COPY rootfs/ /

HEALTHCHECK \
  --interval=5s \
  --timeout=2s \
  --retries=12 \
  CMD ping="$(redis-cli -h "127.0.0.1" ping)" && [[ "$ping" = 'PONG' ]] || exit 1

ENTRYPOINT [ "/usr/bin/redis-server" ]

CMD [ "/etc/redis.conf" ]

# EOF
