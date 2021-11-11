FROM alpine:3.6

MAINTAINER Arve Knudsen <arve.knudsen@gmail.com>

RUN apk update && apk add --no-cache syslog-ng

EXPOSE 514/tcp 514/udp

COPY syslog-ng.conf /etc/
CMD ["/usr/sbin/syslog-ng", "-F", "-f", "/etc/syslog-ng.conf"]
