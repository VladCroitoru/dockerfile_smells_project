FROM alpine:latest
LABEL maintainer="Paul Howell <paul.howell+docker@gmail.com>"

EXPOSE 514 514/udp

VOLUME /var/log

RUN apk add --no-cache rsyslog

CMD ["rsyslogd", "-n"]
