FROM debian:jessie
MAINTAINER Bachue Zhou "bachue.shu@gmail.com"

ENV ETCD_VER v3.1.8
ENV ETCDCTL_API 3

RUN echo "deb http://mirrors.aliyun.com/debian/ jessie main non-free contrib"                  >  /etc/apt/sources.list && \
    echo "deb http://mirrors.aliyun.com/debian/ jessie-proposed-updates main non-free contrib" >> /etc/apt/sources.list && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -qy --no-install-recommends --force-yes wget ca-certificates && \
    rm -rf /var/lib/apt/lists/*

RUN wget -O /etcd-${ETCD_VER}-linux-amd64.tar.gz https://github.com/coreos/etcd/releases/download/${ETCD_VER}/etcd-${ETCD_VER}-linux-amd64.tar.gz && \
    tar xf /etcd-${ETCD_VER}-linux-amd64.tar.gz && \
    rm /etcd-${ETCD_VER}-linux-amd64.tar.gz && \
    mv /etcd-${ETCD_VER}-linux-amd64/etcd /usr/bin/etcd && \
    mv /etcd-${ETCD_VER}-linux-amd64/etcdctl /usr/bin/etcdctl && \
    rm -rf /etcd-${ETCD_VER}-linux-amd64

RUN mkdir /etcd-data
VOLUME /etcd-data
ENV ETCD_DATA_DIR /etcd-data

ENTRYPOINT ["/usr/bin/etcd"]
