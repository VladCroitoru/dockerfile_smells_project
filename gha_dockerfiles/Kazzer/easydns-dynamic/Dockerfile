FROM alpine:latest
LABEL maintainer Kadeem Hassam <docker@peckypanda.com>
LABEL project easydns-dynamic

RUN apk add \
bash \
bind-tools \
curl

COPY easyDNS.sh /opt/easyDNS.sh

ENTRYPOINT ["/opt/easyDNS.sh"]
