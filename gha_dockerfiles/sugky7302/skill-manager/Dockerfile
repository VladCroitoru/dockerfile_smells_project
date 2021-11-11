FROM alpine:latest

RUN set -ex && \
    apk add --no-cache --virtual .lua-builddeps \
        ca-certificates \
        curl \
        gcc \
        libc-dev \
        make \
            readline-dev \
            ncurses-dev && \
    curl -fsSL -o /tmp/lua.tar.gz "https://www.lua.org/ftp/lua-5.4.3.tar.gz" && \
    cd /tmp && \
    echo "ef63ed2ecfb713646a7fcc583cf5f352 *lua.tar.gz" | md5sum -c - && \
    mkdir /tmp/lua && \
    tar -xf /tmp/lua.tar.gz -C /tmp/lua --strip-components=1 && \
    cd /tmp/lua && \
    make linux && \
    make install && \
    cd / && \
    apk add --no-network --no-cache --virtual .lua-rundeps \
        readline \
        ncurses-libs && \
    apk del --no-network .lua-builddeps && \
    rm -rf /tmp/lua /tmp/lua.tar.gz && \
    lua -v

CMD ["lua"]