FROM node:7

MAINTAINER Ivo Marino <ivo.marino@ttss.ch>

LABEL Description="strong-confd-parser" Vendor="TTSS AG" Version="1.0"

ENV \
  DEBIAN_FRONTEND=noninteractive \
  ETCD_VERSION=v3.2.9 \
  # DOWNLOAD_URL="https://github.com/coreos/etcd/releases/download" \
  DOWNLOAD_URL="https://storage.googleapis.com/etcd"

RUN useradd -ms /bin/bash strong-confd-parser && \
    chown -R strong-confd-parser:strong-confd-parser /usr/local &&  \
    su strong-confd-parser -c "npm install -g strongloop && npm cache clear" &&  \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install wget -y && \
    rm -rf /var/lib/apt/lists/* \
    cd /tmp && \
    wget --no-check-certificate ${DOWNLOAD_URL}/${ETCD_VERSION}/etcd-${ETCD_VERSION}-linux-amd64.tar.gz && \
    tar zxvf etcd-*-linux-amd64.tar.gz && \
    cp etcd-*-linux-amd64/etcdctl /usr/local/bin/etcdctl && \
    rm -rf etcd-*-linux-amd64 && \
    chmod +x /usr/local/bin/etcdctl

COPY run.sh /usr/local/bin/run.sh
COPY strong-confd-parse.sh /usr/local/bin/strong-confd-parse.sh

RUN \
  chmod +x /usr/local/bin/run.sh && \
  chmod +x /usr/local/bin/strong-confd-parse.sh

WORKDIR /home/strong-confd-parser
ENV HOME=/home/strong-confd-parser
USER strong-confd-parser

ENTRYPOINT ["run.sh"]
