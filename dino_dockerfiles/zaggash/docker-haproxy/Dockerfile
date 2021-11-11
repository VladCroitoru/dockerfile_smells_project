FROM lsiobase/alpine

LABEL maintainer "zaggash"

ENV DOMAINS=""
ENV EMAIL=""
ENV HAPROXY_VERSION=1.6.9-r1
ENV CERTBOT_VERSION=0.9.3-r0

RUN \
  apk add --no-cache \
    coreutils \
    openssl \
    logrotate \
    certbot \
    inotify-tools \
    haproxy && \

# cleanup
  rm -rf /var/cache/apk/* /tmp/*

# copy local files
COPY root/ /

# ports and volumes
EXPOSE 80 443
VOLUME /config
