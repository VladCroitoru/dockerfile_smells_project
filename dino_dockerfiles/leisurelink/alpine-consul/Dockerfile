FROM leisurelink/alpine-base:1.0.2
MAINTAINER LeisureLink Tech <techteam@leisurelink.com>

# SERVICE_IGNORE is defined in case we're running alongside gliderlabs/registrator; we register ourselves.

ENV CONSUL_VERSION=0.6.4 \
    GLIBC_VERSION=2.21-r2 \
    SERVICE_IGNORE=1

COPY rootfs /

ADD https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip /tmp/consul.zip
ADD https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_web_ui.zip /tmp/consul_web_ui.zip
ADD https://circle-artifacts.com/gh/andyshinn/alpine-pkg-glibc/6/artifacts/0/home/ubuntu/alpine-pkg-glibc/packages/x86_64/glibc-${GLIBC_VERSION}.apk /tmp/glibc-${GLIBC_VERSION}.apk

RUN set -ex && \
    apk --update add drill curl ca-certificates && \
    apk add --allow-untrusted /tmp/glibc-${GLIBC_VERSION}.apk && \
    cd /tmp && \
    mkdir -p /etc/pki/consul \
             /var/data/consul \
             /opt/consul/bin \
             /ui && \
    unzip -d /opt/consul/bin /tmp/consul.zip && \
    ln -s /opt/consul/bin/consul /usr/local/bin/consul && \
    unzip -d /ui consul_web_ui.zip && \
    chmod +x /opt/disco/disco.sh && \
    ln -s /opt/disco/disco.sh /usr/local/bin/disco && \
    rm -rf /tmp/* \
      /var/cache/apk/*
