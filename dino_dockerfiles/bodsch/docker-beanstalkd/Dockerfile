
FROM alpine:3.10 as builder

ARG BUILD_DATE
ARG BUILD_VERSION
ARG BUILD_TYPE
ARG BEANSTALKD_VERSION

# ---------------------------------------------------------------------------------------

WORKDIR /tmp
# hadolint ignore=DL3017,DL3018,DL3019
RUN \
  apk update  --quiet && \
  apk upgrade --quiet && \
  apk add     --quiet \
    build-base \
    git

RUN \
  git clone https://github.com/kr/beanstalkd.git

WORKDIR /tmp/beanstalkd

RUN \
  if [ "${BUILD_TYPE}" = "stable" ] ; then \
    echo "switch to stable Tag v${BEANSTALKD_VERSION}" && \
    git checkout "tags/v${BEANSTALKD_VERSION}" 2> /dev/null ; \
  fi && \
  sed -i 's,sys/fcntl.h,fcntl.h,' sd-daemon.c && \
  make && \
  mv beanstalkd /usr/bin/ && \
  /usr/bin/beanstalkd -v

# ---------------------------------------------------------------------------------------

FROM alpine:3.10

ENV \
  TZ='Europe/Berlin'

EXPOSE 11300
# hadolint ignore=DL3017,DL3018,DL3019
RUN \
  apk update  --quiet --no-cache && \
  apk upgrade --quiet --no-cache && \
  apk add     --quiet --no-cache --virtual .build-deps \
    tzdata && \
  cp "/usr/share/zoneinfo/${TZ}" /etc/localtime && \
  echo "${TZ}" > /etc/timezone && \
  mkdir /var/cache/beanstalkd && \
  apk del --quiet .build-deps && \
  rm -rf \
    /tmp/* \
    /var/cache/apk/

COPY --from=builder /usr/bin/beanstalkd /usr/bin/

HEALTHCHECK \
  --interval=5s \
  --timeout=2s \
  --retries=12 \
  CMD ps ax | grep -v grep | grep -c beanstalkd || exit 1

COPY rootfs/ /
VOLUME [ "/var/cache/beanstalkd" ]

ENTRYPOINT ["/init/run.sh"]

# CMD ["beanstalkd", "-b", "/var/cache/beanstalkd", "-f", "60"]
CMD ["beanstalkd", "-f", "3200"]

# ---------------------------------------------------------------------------------------

LABEL \
  version=${BUILD_VERSION} \
  maintainer="Bodo Schulz <bodo@boone-schulz.de>" \
  org.label-schema.build-date=${BUILD_DATE} \
  org.label-schema.name="beanstalkd Docker Image" \
  org.label-schema.description="Inofficial beanstalkd Docker Image" \
  org.label-schema.url="http://kr.github.io/beanstalkd/" \
  org.label-schema.vcs-url="https://github.com/bodsch/docker-beanstalkd" \
  org.label-schema.vcs-ref=${VCS_REF} \
  org.label-schema.vendor="Bodo Schulz" \
  org.label-schema.version=${BEANSTALKD_VERSION} \
  org.label-schema.schema-version="1.0" \
  com.microscaling.docker.dockerfile="/Dockerfile" \
  com.microscaling.license="The Unlicense"

# ---------------------------------------------------------------------------------------
