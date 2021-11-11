FROM alpine:latest

ENV SS_SCRIPT="https://github.com/shadowsocks/shadowsocks-libev/raw/master/docker/alpine/Dockerfile" \
    SS_URL="https://glare.now.sh/shadowsocks/shadowsocks-libev/.*gz" \
    SS_PORT=8388 \
    SS_PASSWORD="" \
    SS_METHOD="aes-256-cfb" \
    SS_TIMEOUT=300 \
    SS_DNS="8.8.8.8" \
    SS_PARAM=""


RUN set -ex && \
    apk add --no-cache curl && \
    curl -sSL ${SS_SCRIPT} | sed -n '/RUN/{p; :loop; n; /USER/q; p; bloop;}' | sed -e '1s/RUN/   /' | ash

EXPOSE $SS_PORT/tcp

CMD ss-server -s 0.0.0.0 \
              -p $SS_PORT \
              -k $SS_PASSWORD \
              -m $SS_METHOD \
              -t $SS_TIMEOUT \
              --fast-open \
              -d $SS_DNS \
              $SS_PARAM
