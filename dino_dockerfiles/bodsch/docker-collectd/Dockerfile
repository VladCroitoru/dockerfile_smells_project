FROM alpine:3.10

ARG VCS_REF
ARG BUILD_DATE
ARG BUILD_VERSION
ARG BUILD_TYPE
ARG COLLECTD_VERSION

ENV \
  TZ='Europe/Berlin'

# ---------------------------------------------------------------------------------------

SHELL ["/bin/sh", "-o", "pipefail", "-c"]

# hadolint ignore=DL3017,DL3018,DL4006
RUN \
  echo 'hosts: files dns' >> /etc/nsswitch.conf && \
  apk update  --quiet --no-cache && \
  apk upgrade --quiet --no-cache && \
  apk add     --quiet --no-cache --virtual .build-deps \
    shadow \
    tzdata && \
  apk add     --quiet --no-cache \
    bash  \
    collectd \
    collectd-apache \
    collectd-bind \
    collectd-curl \
    collectd-disk \
    collectd-dns \
    collectd-iptables \
    collectd-lvm \
    collectd-mysql \
    collectd-network \
    collectd-nginx \
    collectd-ping \
    collectd-postgresql \
    collectd-python\
    collectd-redis \
    collectd-sensors \
    collectd-utils \
    collectd-virt \
    collectd-write_redis \
    collectd-write_http \
    && \
  version=$(collectd -h | grep "http://collectd" | awk -F ',' '{print $1}') && \
  echo "installed version: ${version}" && \
  echo "export BUILD_DATE=${BUILD_DATE}"              > /etc/profile.d/collectd.sh && \
  echo "export BUILD_VERSION=${BUILD_VERSION}"       >> /etc/profile.d/collectd.sh && \
  echo "export COLLECTD_VERSION=${COLLECTD_VERSION}" >> /etc/profile.d/collectd.sh && \
  cp "/usr/share/zoneinfo/${TZ}" /etc/localtime && \
  echo "${TZ}" > /etc/timezone && \
  mkdir /home/collectd && \
  chown -R collectd:collectd /home/collectd && \
  [ -d /etc/collectd/collectd.d ] || mkdir /etc/collectd/collectd.d && \
  mv /etc/collectd/collectd.conf /etc/collectd/collectd.conf-DIST && \
  apk del --quiet --purge .build-deps && \
  rm -rf \
    /tmp/* \
    /var/cache/apk/*

COPY rootfs/ /

USER collectd
VOLUME ["/etc/collectd/collectd.d","/init/custom.d"]

ENTRYPOINT ["/init/run.sh"]

CMD ["collectd","-f"]

HEALTHCHECK \
  --interval=30s \
  --timeout=2s \
  --retries=10 \
  --start-period=15s \
  CMD /init/healthcheck.sh

# ---------------------------------------------------------------------------------------

LABEL \
  version=${BUILD_VERSION} \
  maintainer="Bodo Schulz <bodo@boone-schulz.de>" \
  org.label-schema.build-date=${BUILD_DATE} \
  org.label-schema.name="Collectd Docker Image" \
  org.label-schema.description="Inofficial Collectd Docker Image" \
  org.label-schema.url="https://collectd.org" \
  org.label-schema.vcs-url="https://github.com/bodsch/docker-collectd" \
  org.label-schema.vcs-ref=${VCS_REF} \
  org.label-schema.vendor="Bodo Schulz" \
  org.label-schema.version=${COLLECTD_VERSION} \
  org.label-schema.schema-version="1.0" \
  com.microscaling.docker.dockerfile="/Dockerfile" \
  com.microscaling.license="Unlicense"

# ---------------------------------------------------------------------------------------
