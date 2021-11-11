FROM alpine:3.3
MAINTAINER Mohit Sharma <mohitsharma44@gmail.com>

RUN apk add --no-cache --update rsync && rm -f /etc/rsyncd.conf

EXPOSE 873
VOLUME /docker
ADD ./run /usr/local/bin/run

ENTRYPOINT ["/usr/local/bin/run"]
