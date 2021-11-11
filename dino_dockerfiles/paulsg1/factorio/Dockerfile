FROM frolvlad/alpine-glibc:alpine-3.6

MAINTAINER https://github.com/dtandersen/docker_factorio_server

ARG USER=factorio
ARG GROUP=factorio
ARG PUID=845
ARG PGID=845

ENV PORT=34197 \
    RCON_PORT=27015

VOLUME /factorio

COPY ./firstrun.sh /tmp

RUN mkdir -p /opt && \
    apk add --update --no-cache pwgen && \
    apk add --update --no-cache --virtual .build-deps curl && \
    mkdir -p /opt/factorio && \
    ln -s /factorio/saves /opt/factorio/saves && \
    ln -s /factorio/mods /opt/factorio/mods && \
    addgroup -g $PGID -S $GROUP && \
    adduser -u $PUID -G $USER -s /bin/sh -SDH $GROUP && \
    chown -R $USER:$GROUP /opt/factorio /factorio /tmp/firstrun.sh && \
    chmod 777 /opt

EXPOSE $PORT/udp $RCON_PORT/tcp

COPY ./docker-entrypoint.sh /

USER $USER

ENTRYPOINT ["/docker-entrypoint.sh"]
