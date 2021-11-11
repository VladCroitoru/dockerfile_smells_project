FROM alpine:3.3
MAINTAINER LeisureLink Tech <techteam@leisurelink.com>

ENV S6_VERSION=1.17.2.0

#
# Light weight process manager overlay, built for docker.
#    see https://github.com/just-containers/s6-overlay to understand why.
#
ADD https://github.com/just-containers/s6-overlay/releases/download/v${S6_VERSION}/s6-overlay-amd64.tar.gz /tmp/s6-overlay.tar.gz

RUN set -ex &&\
    tar xfz /tmp/s6-overlay.tar.gz -C / &&\
    rm -rf /var/cache/apk/* \
           /tmp/*

ENTRYPOINT ["/init"]
