FROM alpine:3.10 as builder

ARG BUILD_DATE
ARG BUILD_VERSION
ARG BUILD_TYPE
ARG VERSION

# ---------------------------------------------------------------------------------------

SHELL ["/bin/sh", "-o", "pipefail", "-c"]

# hadolint ignore=DL3017,DL3018
RUN \
  apk update  --quiet --no-cache && \
  apk upgrade --quiet --no-cache && \
  apk add     --quiet --no-cache \
    automake \
    g++ \
    flex \
    git \
    make \
    musl-dev \
    openssl-dev \
    zlib-dev \
    lz4-dev

RUN \
  echo "export BUILD_DATE=${BUILD_DATE}"            > /etc/profile.d/carbon-c-relay.sh && \
  echo "export BUILD_TYPE=${BUILD_TYPE}"           >> /etc/profile.d/carbon-c-relay.sh

WORKDIR /tmp

RUN \
  git clone https://github.com/grobian/carbon-c-relay.git

WORKDIR /tmp/carbon-c-relay

# hadolint ignore=DL4006,SC2153
RUN \
  if [ "${BUILD_TYPE}" = "stable" ] ; then \
    echo "switch to stable tag v${VERSION}" && \
    git checkout "tags/v${VERSION}" ; \
  fi && \
  version=$(git describe --tags --always | sed 's/^v//') && \
  echo "build version: ${version}"

RUN \
  ./configure && \
  make && make install

CMD ["/bin/sh"]

# ---------------------------------------------------------------------------------------

FROM alpine:3.10

ENV \
  TZ='Europe/Berlin'

# hadolint ignore=DL3018
RUN \
  apk update --quiet --no-cache && \
  apk add    --quiet --no-cache --virtual .build-deps \
    shadow \
    tzdata && \
  apk add    --quiet --no-cache \
    lz4-libs \
    zlib \
    openssl && \
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
  chown -R relay:relay /home/relay && \
  apk del --quiet --purge .build-deps && \
  rm -rf \
    /tmp/* \
    /var/cache/apk/*

COPY --from=builder /etc/profile.d/carbon-c-relay.sh /etc/profile.d/carbon-c-relay.sh
COPY --from=builder /usr/local/bin/relay /usr/bin/
COPY rootfs/ /

WORKDIR /home/relay
USER relay

VOLUME ["/home/relay"]

EXPOSE 2003

HEALTHCHECK \
  --interval=5s \
  --timeout=2s \
  --retries=12 \
  --start-period=10s \
  CMD ps ax | grep -v grep | grep -c relay || exit 1

# ---------------------------------------------------------------------------------------

LABEL \
  version=${BUILD_VERSION} \
  maintainer="Bodo Schulz <bodo@boone-schulz.de>" \
  org.label-schema.build-date=${BUILD_DATE} \
  org.label-schema.name="carbon-relay-ng Docker Image" \
  org.label-schema.description="Inofficial carbon-relay-ng Docker Image" \
  org.label-schema.url="https://github.com/graphite-ng/carbon-relay-ng" \
  org.label-schema.vcs-url="https://github.com/bodsch/docker-docker-carbon-relay-ng" \
  org.label-schema.vcs-ref="${VCS_REF}" \
  org.label-schema.vendor="Bodo Schulz" \
  org.label-schema.version=${VERSION} \
  org.label-schema.schema-version="1.0" \
  com.microscaling.docker.dockerfile="/Dockerfile" \
  com.microscaling.license="The Unlicense"

CMD ["/init/run.sh"]

# ---------------------------------------------------------------------------------------
