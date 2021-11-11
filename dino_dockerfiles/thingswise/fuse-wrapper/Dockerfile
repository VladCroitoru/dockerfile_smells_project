FROM ubuntu 
MAINTAINER Alexander Lukichev

RUN apt-get update
RUN apt-get install -y fuse git wget nano dnsutils pv
RUN apt-get clean all

ENV FLEET_VERSION 0.11.5
ENV ETCDCTL_VERSION 2.1.2

RUN \
  wget -P /tmp https://github.com/coreos/fleet/releases/download/v${FLEET_VERSION}/fleet-v${FLEET_VERSION}-linux-amd64.tar.gz && \
  gunzip /tmp/fleet-v${FLEET_VERSION}-linux-amd64.tar.gz && \
  tar -xf /tmp/fleet-v${FLEET_VERSION}-linux-amd64.tar -C /tmp && \
  mv /tmp/fleet-v${FLEET_VERSION}-linux-amd64/fleetctl /bin/ && \
  rm -rf /tmp/fleet-v${FLEET_VERSION}-linux-amd64*

RUN \
  wget -P /tmp https://github.com/coreos/etcd/releases/download/v${ETCDCTL_VERSION}/etcd-v${ETCDCTL_VERSION}-linux-amd64.tar.gz  && \
  tar xzvf /tmp/etcd-v${ETCDCTL_VERSION}-linux-amd64.tar.gz -C /tmp && \
  mv /tmp/etcd-v${ETCDCTL_VERSION}-linux-amd64/etcdctl /bin/ && \
  rm -rf /tmp/etcd-v${ETCDCTL_VERSION}-linux-amd64*

ADD http://gocfs.s3-website-us-east-1.amazonaws.com/gocfs /gocfs
ADD http://gocfs.s3-website-us-east-1.amazonaws.com/s3repo /s3repo
ADD wrapper.sh /wrapper.sh
RUN chmod +x /gocfs /wrapper.sh /s3repo

VOLUME /cfg

ENTRYPOINT ["/wrapper.sh"]
