FROM alpine:3.13

RUN \
    caddy="https://caddyserver.com/api/download?os=linux&arch=amd64&idempotency=74556302707674"; \
    build="ca-certificates"; \
    run="dumb-init curl jq libcap sudo socat"; \
    \
    apk --update add \
         $build \
         $run \
         && \
    \
    cd /tmp && \
    curl -L $caddy > /caddy && \
    chmod 755 /caddy && \
    setcap cap_net_bind_service=+ep /caddy && \
    rm -rf /tmp/* && \
    \
    mkdir /state && \
    \
    apk del $build && \
    rm -rf /var/cache/apk/*

EXPOSE 80 443
WORKDIR /tmp
VOLUME /state
ENTRYPOINT ["/usr/bin/dumb-init", "--", "/entrypoint.sh"]

ADD entrypoint.sh /
ADD daemon.sh /
