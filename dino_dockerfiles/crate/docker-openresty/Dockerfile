## -*- docker-image-name: "docker-crate" -*-
#
# Openresty Dockerfile
# https://github.com/crate/docker-openresty
#
FROM ubuntu:latest

MAINTAINER Crate Technology GmbH <office@crate.io>

ENV OPENRESTY_VERSION 1.9.3.1

RUN apt-get update \
 && apt-get install -y libreadline-dev libncurses5-dev libpcre3-dev libssl-dev perl make build-essential wget unzip curl \
 && apt-get clean \
 && rm -rf /var/lib/apt \
 && wget -qO- http://openresty.org/download/ngx_openresty-${OPENRESTY_VERSION}.tar.gz | tar xvz -C /root/ \
 && cd /root/ngx_openresty-${OPENRESTY_VERSION} \
 && ./configure \
    --with-ipv6 \
    --with-pcre-jit \
    --with-luajit \
    --with-luajit-xcflags=-DLUAJIT_ENABLE_LUA52COMPAT \
    --http-client-body-temp-path=/var/nginx/client_body_temp \
    --http-proxy-temp-path=/var/nginx/proxy_temp \
    --http-log-path=/logs/openresty/access.log \
    --error-log-path=/logs/openresty/error.log \
    --pid-path=/var/nginx/nginx.pid \
    --lock-path=/var/nginx/nginx.lock \
    --with-http_stub_status_module \
    --with-http_gunzip_module \
    --with-http_realip_module \
    --with-http_ssl_module \
    --with-sha1-asm \
    --with-md5-asm \
    --with-file-aio \
    --without-http_uwsgi_module \
    --without-http_scgi_module \
    --without-http_redis2_module \
 && make \
 && make install \
 && rm -rf /root/ngx_openresty*

VOLUME ["/logs", "/conf", "/data"]

ADD conf/*.conf /conf/

RUN mkdir -p /logs/openresty && mkdir -p /data

WORKDIR /data

EXPOSE 80 443

CMD ["/usr/local/openresty/nginx/sbin/nginx", "-p", "/data", "-c", "/conf/nginx.conf"]

