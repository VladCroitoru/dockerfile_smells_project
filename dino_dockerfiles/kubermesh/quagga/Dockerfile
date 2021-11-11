FROM alpine:3.4

MAINTAINER mike@mikebryant.me.uk

RUN apk --no-cache add quagga

COPY init /sbin/my_init

VOLUME /var/run/quagga

ENTRYPOINT ["/sbin/my_init"]
