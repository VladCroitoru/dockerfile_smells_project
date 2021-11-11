FROM ubuntu:xenial
MAINTAINER Alexander Lukichev

RUN apt-get update
RUN apt-get install -y --fix-missing git nano wget dnsutils sshpass connect-proxy
RUN apt-get clean all

ENV FLEET_VERSION 0.11.8
ENV ETCDCTL_VERSION 2.1.2

# We're using wget where source is immutable, and ADD otherwise

RUN \
  wget -P /tmp https://github.com/coreos/fleet/releases/download/v${FLEET_VERSION}/fleet-v${FLEET_VERSION}-linux-amd64.tar.gz && \
  gunzip /tmp/fleet-v${FLEET_VERSION}-linux-amd64.tar.gz && \
  tar -xf /tmp/fleet-v${FLEET_VERSION}-linux-amd64.tar -C /tmp && \
  mv /tmp/fleet-v${FLEET_VERSION}-linux-amd64/fleetctl /bin/ && \
  rm -rf /tmp/fleet-v${FLEET_VERSION}-linux-amd64*

RUN \
  wget -P /tmp https://github.com/coreos/etcd/releases/download/v${ETCDCTL_VERSION}/etcd-v${ETCDCTL_VERSION}-linux-amd64.tar.gz  && \
  gunzip /tmp/etcd-v${ETCDCTL_VERSION}-linux-amd64.tar.gz && \
  tar -xf /tmp/etcd-v${ETCDCTL_VERSION}-linux-amd64.tar -C /tmp && \
  mv /tmp/etcd-v${ETCDCTL_VERSION}-linux-amd64/etcdctl /bin/ && \
  rm -rf /tmp/etcd-v${ETCDCTL_VERSION}-linux-amd64*

#ADD https://github.com/Yelp/dumb-init/releases/download/v0.5.0/dumb-init_0.5.0_amd64 /dumb-init
RUN wget -P / -O dumb-init https://github.com/Yelp/dumb-init/releases/download/v0.5.0/dumb-init_0.5.0_amd64
ADD http://gocfs.s3-website-us-east-1.amazonaws.com/dcd /dcd
#RUN wget -P / http://gocfs.s3-website-us-east-1.amazonaws.com/dcd
ADD http://gocfs.s3-website-us-east-1.amazonaws.com/s3repo /s3repo
#RUN wget -P / http://gocfs.s3-website-us-east-1.amazonaws.com/s3repo
ADD http://gocfs.s3-website-us-east-1.amazonaws.com/rci /rci
#RUN wget -P / http://gocfs.s3-website-us-east-1.amazonaws.com/rci

RUN chmod +x /dcd /s3repo /rci /dumb-init

ENTRYPOINT ["/dumb-init"]
CMD ["/dcd"]
