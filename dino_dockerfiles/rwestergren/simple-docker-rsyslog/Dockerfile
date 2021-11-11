FROM voxxit/base:alpine

MAINTAINER Randy Westergren <rwestergren (at) xda-developers.com>

RUN  apk add --update rsyslog \
  && rm -rf /var/cache/apk/*

# Send log messages to stdout for viewing with `docker logs`
RUN ln -sf /dev/stdout /var/log/messages

COPY ./etc/rsyslog.conf /etc/rsyslog.conf

EXPOSE 514 514/udp

ENTRYPOINT [ "rsyslogd", "-n" ]

