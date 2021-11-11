FROM debian:jessie

MAINTAINER Shakil Thakur <shakil.thakur@gmail.com> # 2015-12-23

ENV OPENRESTY_VERSION=1.9.7.1 \
 LUAROCKS_VERSION=2.2.2 \
 DEBIAN_FRONTEND=noninteractive

# Install packages.
RUN apt-get update && apt-get install -y \
  automake \
  build-essential \
  libreadline-dev \
  libncurses-dev \
  libpcre3-dev \
  libssl-dev \
  libtool \
  perl \
  unzip \
  wget

# Install openresty
RUN wget -qO- http://openresty.org/download/ngx_openresty-${OPENRESTY_VERSION}.tar.gz | tar xvz -C /root/ \
 && cd /root/ngx_openresty-${OPENRESTY_VERSION} \
 && readonly NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \
 && ./configure --prefix=/opt/openresty --with-http_gunzip_module --with-luajit \
    --with-luajit-xcflags=-DLUAJIT_ENABLE_LUA52COMPAT \
    --http-client-body-temp-path=/var/nginx/client_body_temp \
    --http-proxy-temp-path=/var/nginx/proxy_temp \
    --http-log-path=/var/nginx/access.log \
    --error-log-path=/var/nginx/error.log \
    --pid-path=/var/nginx/nginx.pid \
    --lock-path=/var/nginx/nginx.lock \
    --with-http_stub_status_module \
    --with-http_ssl_module \
    --with-http_realip_module \
    --with-http_v2_module \
    --without-http_fastcgi_module \
    --without-http_uwsgi_module \
    --without-http_scgi_module \
    --with-md5-asm \
    --with-sha1-asm \
    --with-file-aio \
    -j${NPROC} \
 && make -j${NPROC} \
 && make install \
 && rm -rf /root/ngx_openresty* \
 && ln -sf /opt/openresty/nginx/sbin/nginx /usr/local/bin/nginx \
 && ln -sf /usr/local/bin/nginx /usr/local/bin/openresty \
 && ln -sf /opt/openresty/bin/resty /usr/local/bin/resty \
 && ln -sf /opt/openresty/luajit/bin/luajit-2.1.0-beta1 /opt/openresty/luajit/bin/lua \
 && ln -sf /opt/openresty/luajit/bin/lua /usr/local/bin/lua

# install luarocks
RUN wget -qO- http://luarocks.org/releases/luarocks-${LUAROCKS_VERSION}.tar.gz | tar xvz -C /tmp/ \
 && cd /tmp/luarocks-* \
 && ./configure \
    --with-lua=/opt/openresty/luajit/ \
    --lua-suffix=jit-2.1.0-beta1 \
    --with-lua-include=/opt/openresty/luajit/include/luajit-2.1 \
 && make && make install && ldconfig

# install some rocks
RUN mkdir /app
COPY *.rockspec /app/
RUN luarocks build --only-deps /app/*.rockspec

# FINAL SETUP
WORKDIR /app
COPY *.lua /app/
COPY views /app/views
COPY static /app/static
COPY util /app/util
COPY apps /app/apps
COPY mime.types /app/
COPY nginx.conf /app/
# RUN ls
# EXPOSE 80

# CMD lapis server production
