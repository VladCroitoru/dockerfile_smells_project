FROM ubuntu:trusty

MAINTAINER dmitry@feedvisor.com

RUN \
    apt-get update \
 && apt-get -y install \
       curl \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN \
      curl -L  https://github.com/coreos/etcd/releases/download/v2.2.2/etcd-v2.2.2-linux-amd64.tar.gz -o etcd-v2.2.2-linux-amd64.tar.gz \
  &&  tar xzvf etcd-v2.2.2-linux-amd64.tar.gz \
  &&  mv etcd-v2.2.2-linux-amd64 /opt/etcd

ADD entrypoint.sh /entrypoint.sh

CMD bash /entrypoint.sh
