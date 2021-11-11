FROM alpine:3.9
RUN apk update && \
    apk add nginx-mod-http-lua ca-certificates && \
    apk add --virtual build-deps bash build-base curl lua5.1-dev luarocks5.1 openssl-dev && \
    /usr/bin/luarocks-5.1 install luasec && \
    /usr/bin/luarocks-5.1 install lua-Spore && \
    mkdir -p /tmp/src && \
    cd /tmp/src && \
    \
    curl --location -o nginx-crowd-lua.tgz https://github.com/Dwolla/nginx-crowd-lua/archive/master.tar.gz && \
    tar xzvf nginx-crowd-lua.tgz && \
    mkdir -p /etc/nginx/lua /usr/local/share/lua/5.1/Spore/Middleware && \
    cp nginx-crowd-lua-master/crowd-auth.lua /etc/nginx/lua && \
    cp nginx-crowd-lua-master/Spore/Middleware/AdvancedCacheKey.lua /usr/local/share/lua/5.1/Spore/Middleware/AdvancedCacheKey.lua && \
    \
    mkdir -p /run/nginx && \
    ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log && \
    \
    apk del build-deps && \
    rm -rf /tmp/src && \
    rm -rf /var/cache/apk/*

ENTRYPOINT ["nginx"]
CMD ["-g", "daemon off;"]
