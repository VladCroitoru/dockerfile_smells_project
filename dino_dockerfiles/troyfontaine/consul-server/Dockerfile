FROM alpine:3.3
MAINTAINER Troy Fontaine

ENV CONSUL_VERSION 0.6.4
ENV CONSUL_SHA256 abdf0e1856292468e2c9971420d73b805e93888e006c76324ae39416edcf0627
ENV GLIBC_VERSION "2.23-r1"
ENV DNS_RESOLVES consul
ENV DNS_PORT 8600

RUN apk --no-cache add curl ca-certificates && \
    curl -Ls https://github.com/andyshinn/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk > /tmp/glibc-${GLIBC_VERSION}.apk && \
    apk add --no-cache --allow-untrusted /tmp/glibc-${GLIBC_VERSION}.apk && \
    rm -rf /tmp/glibc-${GLIBC_VERSION}.apk
ADD https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip /tmp/consul.zip
RUN echo "${CONSUL_SHA256}  /tmp/consul.zip" > /tmp/consul.sha256 \
  && sha256sum -c /tmp/consul.sha256 \
  && cd /bin \
  && unzip /tmp/consul.zip \
  && chmod +x /bin/consul \
  && rm /tmp/consul.zip
  
ADD ./config /config/
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 8600 8600/udp

ENTRYPOINT ["/bin/consul", "agent", "-server", "-config-dir=/config"]