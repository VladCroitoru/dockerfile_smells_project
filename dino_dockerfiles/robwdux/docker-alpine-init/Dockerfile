FROM robwdux/alpine-base:3.4

MAINTAINER rob dux <robwdux@gmail.com>

ENTRYPOINT ["/init"]

WORKDIR /etc/services.d

# --build-arg ADD_TELEGRAF=true
ARG S6_VERSION=${S6_VERSION:-1.18.1.5}
ARG ADD_CONSUL_TEMPLATE=${ADD_CONSUL_TEMPLATE:-false}
ARG CONSUL_TEMPLATE_VERSION=${CONSUL_TEMPLATE_VERSION:-0.15.0}
ARG ADD_TELEGRAF=${ADD_TELEGRAF:-false}
ARG TELEGRAF_VERSION=${TELEGRAF_VERSION:-0.13.1}

ENV SVC_DIR=/etc/services.d \
    SVC_STG=/etc/services.d/available \
    SVC_TDIR=/etc/services.d/templates \
    # do not reset container env \
    S6_KEEP_ENV=1 \
    # log to stdout and stderr for all services
    S6_LOGGING=0 \
    # warn but continue if any stage 2 code fails
    S6_BEHAVIOUR_IF_STAGE2_FAILS=1 \
    # shared privilege group for services
    SHGRP='' \
    # addons - default enable if installed, allow disabling at runtime
    ENABLE_CONSUL_TEMPLATE='true' \
    CONSUL_DC=dc1 \
    CONSUL_AGENT=127.0.0.1:8500 \
    CONSUL_TEMPLATE_LOG_LEVEL=warn \
    CONSUL_TEMPLATE=/consul-template/test.ctmpl \
    ENABLE_TELEGRAF='true' \
    TELEGRAF_DIR=/telegraf

COPY ./addons/* /addons/

RUN set -o nounset -o errexit -o xtrace -o verbose \
    && apk add --no-cache --virtual .buildDeps gnupg unzip curl ca-certificates \
    && mkdir /usr/src && cd /usr/src \
    # install s6 init
    && curl -fLO \
        https://github.com/just-containers/s6-overlay/releases/download/v${S6_VERSION}/s6-overlay-amd64.tar.gz \
    && curl -fLO \
        https://github.com/just-containers/s6-overlay/releases/download/v${S6_VERSION}/s6-overlay-amd64.tar.gz.sig \
    && curl https://keybase.io/justcontainers/key.asc | gpg --import \
    && gpg --verify s6-overlay-amd64.tar.gz.sig s6-overlay-amd64.tar.gz \
    && tar -C / -zxf s6-overlay-amd64.tar.gz \
    # stage services, template scripts. symlink service to $SVC_DIR to enable
    && mkdir -p $SVC_STG $SVC_TDIR \
    && { \
          echo "#!/bin/sh"; \
          echo "set -o nounset -o errexit -o xtrace -o verbose"; \
      } > ${SVC_TDIR}/run \
    && echo -e "#!/bin/sh\ns6-svscanctl -t /var/run/s6/services" \
        > ${SVC_TDIR}/finish.stop.containers \
    && chmod -R +x ${SVC_TDIR}/* \
    # are there any addons to install?
    && chmod +x /addons/* \
    && /addons/install-addons.sh \
    # purge
    && apk del --purge .buildDeps \
    && cd && rm -vrf /usr/src /root/* /tmp/*

# COMMIT - git show -s --format=%H
# DATE - git show -s --format=%cI
# AUTHOR - git show -s --format='"%an" <%ae>'
# URL - git ls-remote --get-url | sed -e "s|:|/|" -e s|git@|https://|"
ARG GIT_COMMIT=""
ARG GIT_COMMIT_DATE=""
ARG GIT_COMMIT_AUTHOR=""
ARG GIT_REPO_URL=""
