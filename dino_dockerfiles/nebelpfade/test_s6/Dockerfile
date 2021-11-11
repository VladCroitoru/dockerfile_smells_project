FROM alpine:3.2
MAINTAINER Ivan Gaas <ivan.gaas@gmail.com>

ENV TERM="xterm-color" S6_LOGGING="1" S6_LOGGING_SCRIPT="n1 s10000000 T" WODBY_HOME="/srv"
ENV WODBY_DOCROOT="${WODBY_HOME}/docroot" WODBY_FILES="${WODBY_HOME}/files" WODBY_BACKUPS="${WODBY_HOME}/backups" WODBY_LOGS="${WODBY_HOME}/logs" WODBY_CONF="${WODBY_HOME}/conf" WODBY_REPO="${WODBY_HOME}/.repo"
ENV WODBY_STATIC="${WODBY_DOCROOT}/static"

RUN export S6_OVERLAY_VER=1.16.0.0 && \
    addgroup -S -g 1001 wodby && adduser -HS -u 1001 -h ${WODBY_HOME} -s /bin/sh -G wodby wodby && \
    echo 'hosts: files dns' >> /etc/nsswitch.conf && \
    apk add --update ca-certificates && \
    wget -qO- https://github.com/just-containers/s6-overlay/releases/download/v${S6_OVERLAY_VER}/s6-overlay-amd64.tar.gz | tar xz -C / && \
    rm -rf /var/cache/apk/* /tmp/* /usr/bin/su

COPY rootfs /

ENTRYPOINT ["/init"]