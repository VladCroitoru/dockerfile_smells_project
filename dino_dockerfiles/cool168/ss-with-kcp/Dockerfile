FROM alpine:3.12

ENV TZ 'Asia/Shanghai'

ENV SS_LIBEV_VERSION 3.3.5

ENV KCP_VERSION 20210922 

RUN set -ex && \
    apk add --no-cache \
        --virtual .build-deps \
        autoconf \
        build-base \
        curl \
        libev-dev \
        libcap \
        libtool \
        linux-headers \
        libsodium-dev \
        mbedtls-dev \
        pcre-dev \
        tar \
        c-ares-dev && \
    mkdir -p /tmp/ss && \
    cd /tmp/ss && \
    curl -sSL https://github.com/shadowsocks/shadowsocks-libev/releases/download/v$SS_LIBEV_VERSION/shadowsocks-libev-$SS_LIBEV_VERSION.tar.gz | \
    tar xz --strip 1 && \
    ./configure --prefix=/usr --disable-documentation && \
    make install && \
    curl -sSLO https://github.com/xtaci/kcptun/releases/download/v$KCP_VERSION/kcptun-linux-amd64-$KCP_VERSION.tar.gz && \
    tar -zxf kcptun-linux-amd64-$KCP_VERSION.tar.gz && \
    mv server_linux_amd64 /usr/bin/server_linux_amd64 && \
    mv client_linux_amd64 /usr/bin/client_linux_amd64 && \       
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone && \    
    rm -rf kcptun-linux-amd64-$KCP_VERSION.tar.gz && \    
    ls /usr/bin/ss-* | xargs -n1 setcap 'cap_net_bind_service+ep' && \
    runDeps="$( \
        scanelf --needed --nobanner /usr/bin/ss-* \
            | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
            | xargs -r apk info --installed \
            | sort -u \
    )" && \
    apk add --no-cache --virtual .run-deps $runDeps && \
    apk del .build-deps && \
    apk add --no-cache privoxy \
        rng-tools && \    
    cd / && rm -rf /tmp/* 
    
ADD kcp2ss-server.sh /kcp2ss-server.sh
ADD ss2kcp-client.sh /ss2kcp-client.sh
ADD ss-local.sh /ss-local.sh
ADD ss-server.sh /ss-server.sh
ADD p2ss2kcp-client.sh /p2ss2kcp-client.sh
ADD kcp-client.sh /kcp-client.sh
ADD kcp-server.sh /kcp-server.sh
RUN chmod +x /*.sh
