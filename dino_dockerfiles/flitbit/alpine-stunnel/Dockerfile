FROM alpine:3.2
MAINTAINER Phillip Clark <phillip@flitbit.com>

COPY rootfs /

RUN set -ex &&\
    echo "http://dl-3.alpinelinux.org/alpine/edge/testing/" >> /etc/apk/repositories &&\
    apk update && apk add --update stunnel &&\
    chmod +x /opt/run-stunnel.sh &&\
    rm -rf /tmp/* \
           /var/cache/apk/*

EXPOSE 4442

ENTRYPOINT ["/opt/run-stunnel.sh"]
