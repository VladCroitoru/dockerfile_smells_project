FROM alpine:3.9.3

ENV NGINX_VERSION release-1.16.0
ENV LUAJIT_VERSION 2.0.5
ENV LUA_NGX_MODULE_VERSION 0.10.14
ENV LUA_RESTY_DNS_VERSION 0.21
ENV NGINX_DEV_KIT_VERSION 0.3.0

RUN apk add --no-cache ca-certificates pcre libldap libgcc libressl \
  && apk add --no-cache --virtual build-dependencies \
       build-base \
       pcre-dev \
       git \
       zlib-dev \
       openssh-client \
       openldap-dev \
       libressl-dev \
  && cd ~ \
  && wget -O luajit.tar.gz http://luajit.org/download/LuaJIT-${LUAJIT_VERSION}.tar.gz \
  && tar zxvf luajit.tar.gz \
  && cd LuaJIT-${LUAJIT_VERSION} \
  && make \
  && make install \
  && cd ~ \
  && rm -rf luajit.tar.gz LuaJIT-${LUAJIT_VERSION} \
  && mkdir -p \
       /etc/nginx \
       /var/lib/nginx/body \
       /var/lib/nginx/fastcgi \
       /var/lib/nginx/proxy \
       /var/log/nginx \
  && cd ~ \
  && wget -O ngx_devel_kit.tar.gz https://github.com/simpl/ngx_devel_kit/archive/v${NGINX_DEV_KIT_VERSION}.tar.gz \
  && tar zxvf ngx_devel_kit.tar.gz \
  && rm ngx_devel_kit.tar.gz \
  && wget -O ngx_lua.tar.gz https://github.com/openresty/lua-nginx-module/archive/v${LUA_NGX_MODULE_VERSION}.tar.gz \
  && tar zxvf ngx_lua.tar.gz \
  && rm ngx_lua.tar.gz \
  && export LUAJIT_LIB=/usr/local/lib \
  && export LUAJIT_INC=/usr/local/include/luajit-2.0 \
  && git clone https://github.com/kvspb/nginx-auth-ldap.git \
  && git clone https://github.com/nginx/nginx.git \
  && git clone https://github.com/GUI/nginx-upstream-dynamic-servers.git \
  && cd ~/nginx \
  && git checkout tags/${NGINX_VERSION} \
  && ./auto/configure \
    --with-ld-opt="-Wl,-rpath,/usr/local/lib" \
    --add-module=/root/ngx_devel_kit-${NGINX_DEV_KIT_VERSION} \
    --add-module=/root/lua-nginx-module-${LUA_NGX_MODULE_VERSION} \
    --add-module=/root/nginx-auth-ldap \
    --add-module=/root/nginx-upstream-dynamic-servers \
    --http-client-body-temp-path=/var/lib/nginx/body \
    --http-fastcgi-temp-path=/var/lib/nginx/fastcgi \
    --http-proxy-temp-path=/var/lib/nginx/proxy \
    --with-http_ssl_module \
    --with-http_realip_module \
    --with-http_auth_request_module \
    --with-debug \
    --conf-path=/etc/nginx/nginx.conf \ 
    --sbin-path=/usr/sbin/nginx \ 
    --pid-path=/var/run/nginx.pid \ 
    --error-log-path=/var/log/nginx/error.log \ 
    --http-log-path=/var/log/nginx/access.log \
  && make -j$(getconf _NPROCESSORS_ONLN) \
  && make install \
  && ln -s /usr/local/lib/libluajit-5.1.so /usr/lib/libluajit-5.1.so.2 \
  && wget -O /usr/local/share/luajit-${LUAJIT_VERSION}/dns_resolver.lua https://raw.githubusercontent.com/openresty/lua-resty-dns/v${LUA_RESTY_DNS_VERSION}/lib/resty/dns/resolver.lua \
  && cd ~ \
  && rm -rf ngx_devel_kit-${NGINX_DEV_KIT_VERSION} \
  && rm -rf lua-nginx-module-${LUA_NGX_MODULE_VERSION} \
  && rm -rf nginx-auth-ldap \
  && rm -rf nginx \
  && apk del build-dependencies

COPY srv_router.lua /etc/nginx/

CMD ["/usr/sbin/nginx","-g","daemon off;"]
