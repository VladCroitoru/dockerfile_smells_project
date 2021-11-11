FROM alpine:latest
MAINTAINER Thibault NORMAND <me@zenithar.org>

RUN apk add --update -t build-deps wget unzip \
    && wget --no-check-certificate https://github.com/coreos/etcd/releases/download/v2.2.2/etcd-v2.2.2-linux-amd64.tar.gz \
    && tar zxvf etcd-v2.2.2-linux-amd64.tar.gz \
    && mv etcd-v2.2.2-linux-amd64/etcd /usr/bin/etcd \
    && chmod +x /usr/bin/etcd \
    && mv etcd-v2.2.2-linux-amd64/etcdctl /usr/bin/etcdctl \
    && chmod +x /usr/bin/etcdctl \
    && rm -f etcd-v2.2.2-linux-amd64.tar.gz \
    && mkdir /data \
    && addgroup etcd \
    && adduser -s /bin/false -G etcd -S -D etcd \
    && apk del --purge build-deps \
    && rm -rf /var/cache/apk/*

USER        etcd
EXPOSE      2979 2980 4001 7001
VOLUME      ["/data"]
WORKDIR     /data
ENTRYPOINT  ["/usr/bin/etcd"]
