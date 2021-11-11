#
# Alpine linux docker image with Unbound DNS
#
# Unbound is preconfigured as forwarding DNS with aggressive caching
# and forwarding to CloudFlare and Google Public DNSes
#

FROM alpine:latest

MAINTAINER Chris Kruszynski <thywolf@gmail.com>

RUN apk add --no-cache --update unbound

COPY unbound.conf /etc/unbound/unbound.conf

RUN unbound-checkconf

EXPOSE 53
EXPOSE 53/udp

CMD ["unbound"]
