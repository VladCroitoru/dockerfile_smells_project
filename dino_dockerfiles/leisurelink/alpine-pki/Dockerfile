FROM leisurelink/alpine-base
MAINTAINER LeisureLink Tech <techteam@leisurelink.com>

ENV S6_BEHAVIOUR_IF_STAGE2_FAILS=2

COPY rootfs /

RUN set -ex && \
    apk --update add openssl curl ca-certificates inotify-tools && \
    rm -rf /tmp/* \
      /var/cache/apk/*
