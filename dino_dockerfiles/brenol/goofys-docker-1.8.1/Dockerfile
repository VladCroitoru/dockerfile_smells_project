FROM golang:1.8.1-alpine

MAINTAINER Breno Loyola

RUN apk update && apk add gcc ca-certificates openssl musl-dev git fuse

# Goofys
RUN go get github.com/kahing/goofys
RUN go install github.com/kahing/goofys

# add syslog-ng (syslog required by Goofys)
RUN apk add syslog-ng
RUN echo "@version: 3.7" > /etc/syslog-ng/syslog-ng.conf
RUN echo "source s_local {internal();network(transport("udp"));unix-dgram("/dev/log");};" >> /etc/syslog-ng/syslog-ng.conf
RUN echo "destination d_local {file("/var/log/messages");};" >> /etc/syslog-ng/syslog-ng.conf
RUN echo "log {source(s_local);destination(d_local);};" >> /etc/syslog-ng/syslog-ng.conf

RUN mkdir /mnt/s3

ENV MOUNT_DIR /mnt/s3
ENV REGION eu-west-1
ENV BUCKET my-bucket
ENV STAT_CACHE_TTL 1m0s
ENV TYPE_CACHE_TTL 1m0s
ENV DIR_MODE 0500
ENV FILE_MODE 0500

ADD ./bin/run.sh /root/run.sh

ENTRYPOINT ["sh"]
CMD ["/root/run.sh"]
