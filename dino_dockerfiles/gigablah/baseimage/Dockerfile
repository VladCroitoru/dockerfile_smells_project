FROM gliderlabs/alpine:3.1
MAINTAINER Chris Heng <bigblah@gmail.com>

ADD s6-2.0.0.1.tar.gz /
ADD service /etc/service

RUN mkdir -p /var/spool/cron/crontabs

ENTRYPOINT ["/usr/bin/s6-svscan", "-t0"]
CMD ["/etc/service"]
