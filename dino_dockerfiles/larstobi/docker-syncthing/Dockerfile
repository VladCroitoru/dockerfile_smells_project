FROM alpine:edge
MAINTAINER Lars Tobias Skjong-Børsting <larstobi@relatime.no>

ARG SYNCTHING_VERSION=0.14.6

ENV SYNCTHING_DATA=/data
ENV SYNCTHING_HOME=/syncthing

ADD resources/syncthing.sh /syncthing/syncthing.sh

RUN set -x \
 && apk add --no-cache bash \
 && apk add --no-cache \
    --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ \
    xmlstarlet \
 && apk add --no-cache --virtual .build-deps \
      curl \
        ca-certificates \
 && adduser -D -h $SYNCTHING_HOME user \
 && mkdir -p ${SYNCTHING_DATA} \
 && chown user ${SYNCTHING_DATA} \
 && curl -L -o syncthing.tar.gz https://github.com/syncthing/syncthing/releases/download/v$SYNCTHING_VERSION/syncthing-linux-amd64-v$SYNCTHING_VERSION.tar.gz \
 && tar -xzvf syncthing.tar.gz \
 && rm -f syncthing.tar.gz \
 && mv syncthing-linux-amd64-v* $SYNCTHING_HOME/syncthing \
 && rm -rf $SYNCTHING_HOME/syncthing/etc \
 && rm -rf $SYNCTHING_HOME/syncthing/*.pdf \
 && chmod 777 /syncthing/syncthing.sh \
 && apk del .build-deps

USER user
WORKDIR $SYNCTHING_HOME
VOLUME ["$SYNCTHING_HOME"]
ENTRYPOINT ["/syncthing/syncthing.sh"]
