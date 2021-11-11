FROM alpine:3.3

MAINTAINER Dan Streeter <dan@danstreeter.co.uk>

RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories && apk add --update whois

ENTRYPOINT ["/bin/sh", "-c", "whois ${*}", "--"]
