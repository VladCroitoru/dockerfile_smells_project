#
# Dockerfile for ShadowsocksR
#

FROM alpine:3.11

ENV SSR_URL https://github.com/shadowsocksrr/shadowsocksr/archive/akkariiin/master.tar.gz
ENV SSR_DIR shadowsocksr-akkariiin-master

WORKDIR /etc

RUN set -ex \
    && apk --update add --no-cache python libsodium rng-tools curl \
    && curl -sSL $SSR_URL | tar xz \
    && apk del curl \
    && rm -rf /var/cache/apk

ENV SERVER_ADDR 0.0.0.0
ENV SERVER_PORT 8388
ENV PASSWORD    p@ssw0rd
ENV METHOD      chacha20-ietf
ENV PROTOCOL    auth_aes128_md5
ENV OBFS        tls1.2_ticket_auth
ENV TIMEOUT     300

WORKDIR /etc/$SSR_DIR/shadowsocks

CMD python server.py \
           -s $SERVER_ADDR \
           -p $SERVER_PORT \
           -k $PASSWORD    \
           -m $METHOD      \
           -O $PROTOCOL    \
           -o $OBFS        \
           -t $TIMEOUT
