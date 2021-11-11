# Shadowsocks Server with KCPTUN support Dockerfile

FROM imhang/shadowsocks-docker

ENV KCP_VER 20161202

RUN \
    apk add --no-cache --virtual .build-deps curl \
    && mkdir -p /opt/kcptun \
    && cd /opt/kcptun \
    && curl -fSL https://github.com/xtaci/kcptun/releases/download/v$KCP_VER/kcptun-linux-amd64-$KCP_VER.tar.gz | tar xz \
    && rm client_linux_amd64 \
    && cd ~ \
    && apk del .build-deps \
    && apk add --no-cache supervisor

ENV KCP_PORT=9443 KCP_MODE=fast2 MTU=1400 SNDWND=2048 RCVWND=2048 CRYPT=xor DATASHARD=10 PARITYSHARD=0 KCPTUN_KEY="it's a secrect" SS_DNS1=8.8.8.8 SS_DNS2=8.8.4.4
COPY supervisord.conf /etc/supervisord.conf

EXPOSE $KCP_PORT/udp

ENTRYPOINT ["/usr/bin/supervisord"]

