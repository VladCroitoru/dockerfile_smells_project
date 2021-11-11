FROM robwdux/docker-alpine-base

MAINTAINER rob dux <robwdux@gmail.com>

ENV S6_VERSION=1.16.0.0 \
    SVC_TL_DIR=/etc/s6/svc-templates \
    SVC_DIR=/etc/services.d

RUN set -o nounset -o errexit -o xtrace -o verbose && \
    curl -sSL https://github.com/just-containers/s6-overlay/releases/download/v${S6_VERSION}/s6-overlay-amd64.tar.gz \
      | tar -zxf - -C / && \
    mkdir -p $SVC_TL_DIR && \
    echo "#!/usr/bin/with-contenv sh" \
      > ${SVC_TL_DIR}/run.container.env && \
    echo -e "#!/bin/sh\ns6-svscanctl -t /var/run/s6/services" \
      > ${SVC_TL_DIR}/finish.stop.container && \
    chmod -R +x ${SVC_TL_DIR}/*

ENTRYPOINT ["/init"]
