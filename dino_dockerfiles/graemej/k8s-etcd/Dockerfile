# Dockerfile for running an etcd (primarily in Kubernetes)

FROM ubuntu:trusty

MAINTAINER Graeme Johnson <graeme@johnson-family.ca>

RUN \
 sed 's/main$/main universe/' -i /etc/apt/sources.list && \
 apt-get update && \
 env DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-common python-software-properties curl

RUN \
 cd /tmp && \
 (curl -L  https://github.com/coreos/etcd/releases/download/v0.4.6/etcd-v0.4.6-linux-amd64.tar.gz | tar -xz) && \
 mkdir -p /opt/etcd/bin && \
 cp -v /tmp/etcd-v0.4.6-linux-amd64/etcd /opt/etcd/bin && \
 cp -v /tmp/etcd-v0.4.6-linux-amd64/etcdctl /opt/etcd/bin && \
 rm -rf /tmp/etcd-v0.4.6-linux-amd64

WORKDIR /opt/etcd

EXPOSE 4001 7001

VOLUME ["/opt/etcd/conf", "/opt/etcd/data", "/opt/etcd/log"]

ADD config-and-run.sh /opt/etcd/bin/

ENTRYPOINT ["/opt/etcd/bin/config-and-run.sh"]
CMD [""]
