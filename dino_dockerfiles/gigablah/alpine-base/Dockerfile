FROM alpine:3.2
MAINTAINER Chris Heng <bigblah@gmail.com>

RUN apk add -U bash && rm -rf /var/cache/apk/*
ADD s6-overlay-amd64.tar.gz /
COPY rootfs /

ENTRYPOINT ["/init"]
