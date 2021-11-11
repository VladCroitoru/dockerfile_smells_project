FROM alpine:edge

MAINTAINER Tomasz Jezierski <developers@tefnet.pl>

RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories && apk add --no-cache mongodb-tools aws-cli

ADD backup.sh /usr/local/bin/backup

CMD /usr/local/bin/backup
