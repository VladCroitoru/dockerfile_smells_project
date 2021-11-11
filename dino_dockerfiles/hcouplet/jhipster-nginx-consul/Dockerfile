FROM alpine:3.6
#inspired from https://github.com/bhuisgen/docker-alpine
MAINTAINER Hervé COUPLET <herve.couplet@creativeone.eu>

ENV S6OVERLAY_VERSION=v1.20.0.0 \
    CONSUL_VERSION=0.9.3 \
    S6_BEHAVIOUR_IF_STAGE2_FAILS=1 \
    LANG=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    TERM=xterm

RUN apk update && apk upgrade && \
    apk add bash bind-tools ca-certificates curl jq tar && \
    curl -sSL https://github.com/just-containers/s6-overlay/releases/download/${S6OVERLAY_VERSION}/s6-overlay-amd64.tar.gz | tar xz -C /

RUN mkdir -p /var/lib/consul && \
    addgroup -g 500 -S consul && \
    adduser -u 500 -S -D -g "" -G consul -s /sbin/nologin -h /var/lib/consul consul && \
    chown -R consul:consul /var/lib/consul

RUN apk add --update zip && \
    curl -sSL https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip -o /tmp/consul.zip && \
    unzip /tmp/consul.zip -d /bin && \
    rm /tmp/consul.zip && \
    apk del zip

RUN apk add --update nginx

RUN apk del tar && \
    rm -rf /var/cache/apk/*

COPY rootfs/ /

ENTRYPOINT ["/init"]
CMD []

EXPOSE 80 443
VOLUME [ "/var/lib/consul", "/var/cache/nginx", "/var/www" ]

HEALTHCHECK CMD /etc/consul.d/check || exit 1

