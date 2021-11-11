FROM alpine:edge


RUN apk update \
    && apk add python libsodium unzip wget \
    && rm -rf /var/cache/apk/*

RUN mkdir /ssr \
    && cd /ssr \
    && wget --no-check-certificate https://github.com/breakwa11/shadowsocks/archive/manyuser.zip -O /tmp/manyuser.zip \
    && unzip -d /tmp /tmp/manyuser.zip \
    && mv /tmp/shadowsocksr-manyuser/shadowsocks /ssr/shadowsocks \
    && rm -rf /tmp/*

ENV KCP_VER 20170218

RUN \
    apk add --no-cache --virtual .build-deps curl \
    && mkdir -p /opt/kcptun \
    && cd /opt/kcptun \
    && curl -fSL https://github.com/xtaci/kcptun/releases/download/v$KCP_VER/kcptun-linux-amd64-$KCP_VER.tar.gz | tar xz \
    && rm client_linux_amd64 \
    && cd ~ \
    && apk del .build-deps \
    && apk add --no-cache supervisor
    
ADD init.sh /ssr/init.sh
RUN chmod +x /ssr/init.sh
COPY user-config.json /opt/shadowsocks/
COPY supervisord.conf /etc/supervisor/
COPY ssr.conf /etc/supervisor/conf.d/

ADD start.sh /start.sh
RUN chmod +x /start.sh
COPY kcp.conf /etc/supervisor/conf.d/

EXPOSE 8989/tcp 8989/udp 29900/udp
ENTRYPOINT ["/bin/sh","/ssr/init.sh"]
#ENTRYPOINT ["/usr/bin/supervisord","-n","-c", "/etc/supervisor/supervisord.conf"]
