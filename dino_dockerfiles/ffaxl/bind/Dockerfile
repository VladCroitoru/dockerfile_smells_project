FROM alpine:latest
MAINTAINER Evgeniy Slizevich <evgeniy@slizevich.net>

WORKDIR /

RUN apk add --no-cache bind
ADD bind bind

EXPOSE 53/udp 53/tcp
VOLUME [/etc/bind]

ENTRYPOINT ["/bind"]
