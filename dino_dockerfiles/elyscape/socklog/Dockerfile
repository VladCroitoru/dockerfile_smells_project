FROM alpine:3.5

MAINTAINER Eli Young <elyscape@gmail.com>

RUN apk add --no-cache socklog

EXPOSE 8514/udp

CMD ["/sbin/socklog", "inet", "0", "8514"]
