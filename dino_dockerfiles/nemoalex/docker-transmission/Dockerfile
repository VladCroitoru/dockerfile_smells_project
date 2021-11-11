FROM alpine:edge
MAINTAINER Nemo Alex <zhhjchina@gmail.com>

RUN set -xe \
    && apk add --no-cache transmission-daemon

VOLUME ["/root/Downloads", "/etc/transmission-daemon"]

EXPOSE 9091 51413/tcp 51413/udp

CMD ["transmission-daemon", "-f", "--config-dir", "/etc/transmission-daemon", "--log-error"]
