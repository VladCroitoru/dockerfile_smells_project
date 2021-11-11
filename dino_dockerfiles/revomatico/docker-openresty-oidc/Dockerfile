FROM alpine:3.10
MAINTAINER Cristian Chiru <cristian.chiru@revomatico.com>

ENV LUA_SUFFIX=jit-2.1.0-beta3 \
    LUAJIT_VERSION=2.1 \
    NGINX_PREFIX=/opt/openresty/nginx \
    OPENRESTY_PREFIX=/opt/openresty \
    OPENRESTY_SRC_SHA256=bf92af41d3ad22880047a8b283fc213d59c7c1b83f8dae82e50d14b64d73ac38 \
    OPENRESTY_VERSION=1.15.8.2 \
    LUAROCKS_VERSION=3.1.3 \
    LUAROCKS_SRC_SHA256=c573435f495aac159e34eaa0a3847172a2298eb6295fcdc35d565f9f9b990513 \
    LUA_RESTY_OPENIDC_VERSION=1.7.2-1 \
    VAR_PREFIX=/var/nginx

RUN set -ex \
  && apk --no-cache add \
    libgcc \
    libpcrecpp \
    libpcre16 \
    libpcre32 \
    libssl1.1 \
    libstdc++ \
    openssl \
    pcre \
    curl \
    unzip \
    git \
    dnsmasq \
  && apk --no-cache add --virtual .build-dependencies \
    make \
    musl-dev \
    gcc \
    ncurses-dev \
    openssl-dev \
    pcre-dev \
    perl \
    readline-dev \
    zlib-dev \
    libc-dev \
  \
## OpenResty
  && curl -fsSL https://github.com/openresty/openresty/releases/download/v${OPENRESTY_VERSION}/openresty-${OPENRESTY_VERSION}.tar.gz -o /tmp/openresty.tar.gz \
  \
  && cd /tmp \
  && echo "${OPENRESTY_SRC_SHA256} *openresty.tar.gz" | sha256sum -c - \
  && tar -xzf openresty.tar.gz \
  \
  && cd openresty-* \
  && readonly NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \
  && ./configure \
    --prefix=${OPENRESTY_PREFIX} \
    --http-client-body-temp-path=${VAR_PREFIX}/client_body_temp \
    --http-proxy-temp-path=${VAR_PREFIX}/proxy_temp \
    --http-log-path=${VAR_PREFIX}/access.log \
    --error-log-path=${VAR_PREFIX}/error.log \
    --pid-path=${VAR_PREFIX}/nginx.pid \
    --lock-path=${VAR_PREFIX}/nginx.lock \
    --with-luajit \
    --with-pcre-jit \
    --with-ipv6 \
    --with-http_ssl_module \
    --without-http_ssi_module \
    --with-http_realip_module \
    --without-http_scgi_module \
    --without-http_uwsgi_module \
    --without-http_userid_module \
    -j${NPROC} \
  && make -j${NPROC} \
  && make install \
  \
  && rm -rf /tmp/openresty* \
  \
## LuaRocks
  && curl -fsSL http://luarocks.github.io/luarocks/releases/luarocks-${LUAROCKS_VERSION}.tar.gz -o /tmp/luarocks.tar.gz \
  \
  && cd /tmp \
  && echo "${LUAROCKS_SRC_SHA256} *luarocks.tar.gz" | sha256sum -c - \
  && tar -xzf luarocks.tar.gz \
  \
  && cd luarocks-* \
  && ./configure \
    --prefix=${OPENRESTY_PREFIX}/luajit \
    --lua-suffix=${LUA_SUFFIX} \
    --with-lua=${OPENRESTY_PREFIX}/luajit \
    --with-lua-lib=${OPENRESTY_PREFIX}/luajit/lib \
    --with-lua-include=${OPENRESTY_PREFIX}/luajit/include/luajit-${LUAJIT_VERSION} \
  && make build \
  && make install \
  \
  && rm -rf /tmp/luarocks* \
  && rm -rf ~/.cache/luarocks \
## Post install
  && ln -sf ${NGINX_PREFIX}/sbin/nginx /usr/local/bin/nginx \
  && ln -sf ${NGINX_PREFIX}/sbin/nginx /usr/local/bin/openresty \
  && ln -sf ${OPENRESTY_PREFIX}/bin/resty /usr/local/bin/resty \
  && ln -sf ${OPENRESTY_PREFIX}/luajit/bin/luajit-* ${OPENRESTY_PREFIX}/luajit/bin/lua \
  && ln -sf ${OPENRESTY_PREFIX}/luajit/bin/luajit-* /usr/local/bin/lua  \
  && ln -sf ${OPENRESTY_PREFIX}/luajit/bin/luarocks /usr/local/bin/luarocks \
  && ln -sf ${OPENRESTY_PREFIX}/luajit/bin/luarocks-admin /usr/local/bin/luarocks-admin \
  && echo user=root >> /etc/dnsmasq.conf \
## Install lua-resty-openidc
  && cd ~/ \
  # Fix for https://github.com/zmartzone/lua-resty-openidc/issues/213#issuecomment-432471572
#  && luarocks install lua-resty-hmac \
  && luarocks install lua-resty-openidc ${LUA_RESTY_OPENIDC_VERSION} \
## Install lua-resty-xacml-pep
#  && curl -fsSL https://raw.githubusercontent.com/zmartzone/lua-resty-xacml-pep/master/lib/resty/xacml_pep.lua -o /opt/openresty/lualib/resty/xacml_pep.lua \
## Cleanup
  && apk del .build-dependencies 2>/dev/null

WORKDIR $NGINX_PREFIX

CMD dnsmasq; openresty -g "daemon off; error_log /dev/stderr info;"
