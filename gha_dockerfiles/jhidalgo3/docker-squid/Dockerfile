
FROM alpine:3.13.5

MAINTAINER Jose Maria Hidalgo <jhidalgo3@gmail.com>

RUN apk update \
    && apk upgrade \
    && apk add squid \
    && rm -rf /var/cache/apk/*

CMD ["sh", "-c", "(tail -F /var/log/squid/access.log &) && /usr/sbin/squid -f /etc/squid/squid.conf -NYCd 1"]
