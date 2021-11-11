FROM alpine:latest

LABEL maintainer="letssudormrf"

ENV V2_GIT_PATH="https://github.com/v2ray/v2ray-core"
ENV V2_VERSION="latest"
ENV V2_PORT="8880"
ENV HTTP_PORT="8080"
ENV HTTPS_PORT="8443"
ENV CADDY_PLUGINS="http.forwardproxy"
ENV CADDYPATH="/tmp/"
ENV V2RAY_LOCATION_ASSET="/usr/local/bin/"
ENV V2RAY_LOCATION_CONFIG="/tmp/"
ENV V2RAY_RAY_BUFFER_SIZE="2"
ENV V2RAY_BUF_READV="auto"

RUN apk add --no-cache --virtual .buildDeps curl bash gnupg \
    && apk add --no-cache --virtual .gettext gettext \
    && runDeps="$(scanelf --needed --nobanner --format '%n#p' /usr/bin/envsubst | tr ',' '\n' | sort -u | awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1 }')" \
    && apk add --no-cache ca-certificates $runDeps \
    && curl https://getcaddy.com | bash -s personal ${CADDY_PLUGINS} \
    && VER=$(curl --silent https://api.github.com/repos/${V2_GIT_PATH#**//*/}/releases/${V2_VERSION} | grep '"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/') \    
    && curl -L -H "Cache-Control: no-cache" -o /tmp/v2.zip ${V2_GIT_PATH}/releases/download/$VER/v2ray-linux-64.zip \
    && unzip -j /tmp/v2.zip "v2ray" "v2ctl" "geoip.dat" "geosite.dat" -d /usr/local/bin/ \
    && mv /usr/bin/envsubst /usr/local/bin/ \
    && apk del .buildDeps \
    && apk del .gettext \
    && rm -rf /tmp/*

COPY entrypoint.sh /usr/local/bin/
COPY v2cfg /usr/local/share/v2cfg
COPY caddycfg /usr/local/share/caddycfg

RUN chmod a+rwx /usr/local/bin/entrypoint.sh /usr/local/bin/v2ray /usr/local/bin/v2ctl

WORKDIR /tmp

EXPOSE 8443/tcp 8080/tcp 8880/tcp

CMD ["entrypoint.sh"]
