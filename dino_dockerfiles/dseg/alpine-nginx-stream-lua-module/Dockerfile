FROM alpine:3.3
MAINTAINER Daichi Shinozaki <dsdseg@gmail.com>
# Based on excellent Dockerfile by Adrian B. Danieli (https://github.com/sickp/docker-alpine-nginx)

ENV NGINX_VERSION=1.9.11
ENV STREAM_LUA_MODULE_VERSION=0.0.1
ENV STREAM_ECHO_MODULE_VERSION=master

ENV LUAJIT_LIB=/usr/lib
ENV LUAJIT_INC=/usr/include/luajit-2.0

RUN \
  apk --no-cache add --virtual makedepends build-base linux-headers openssl-dev pcre-dev curl zlib-dev luajit-dev && \
  apk --no-cache add ca-certificates openssl pcre zlib luajit && \
  cd /tmp && \
  curl -sL http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz | tar xvz && \
  curl -sL https://github.com/openresty/stream-lua-nginx-module/archive/${STREAM_LUA_MODULE_VERSION}.tar.gz | tar xvz && \
  curl -sL https://github.com/openresty/stream-echo-nginx-module/archive/${STREAM_ECHO_MODULE_VERSION}.tar.gz | tar xvz && \
  cd /tmp/nginx-${NGINX_VERSION} && \
  ./configure \
    --with-cc-opt="-Wno-error" \
    --prefix=/etc/nginx \
    --sbin-path=/usr/sbin/nginx \
    --conf-path=/etc/nginx/nginx.conf \
    --error-log-path=/var/log/nginx/error.log \
    --http-log-path=/var/log/nginx/access.log \
    --pid-path=/var/run/nginx.pid \
    --lock-path=/var/run/nginx.lock \
    --http-client-body-temp-path=/var/cache/nginx/client_temp \
    --http-proxy-temp-path=/var/cache/nginx/proxy_temp \
    --http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \
    --http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \
    --http-scgi-temp-path=/var/cache/nginx/scgi_temp \
    --user=nginx \
    --group=nginx \
    --with-http_ssl_module \
    --with-http_realip_module \
    --with-http_addition_module \
    --with-http_sub_module \
    --with-http_dav_module \
    --with-http_flv_module \
    --with-http_mp4_module \
    --with-http_gunzip_module \
    --with-http_gzip_static_module \
    --with-http_random_index_module \
    --with-http_secure_link_module \
    --with-http_stub_status_module \
    --with-http_auth_request_module \
    --with-mail \
    --with-mail_ssl_module \
    --with-file-aio \
    --with-ipv6 \
    --with-threads \
    --with-stream \
    --with-stream_ssl_module \
    --with-http_v2_module \
    --with-pcre-jit \
    --add-module="../stream-lua-nginx-module-${STREAM_LUA_MODULE_VERSION}" \
    --add-module="../stream-echo-nginx-module-${STREAM_ECHO_MODULE_VERSION}" \
    && \
  make install && \
  sed -i -e 's/#access_log  logs\/access.log  main;/access_log \/dev\/stdout;/' -e 's/#error_log  logs\/error.log  notice;/error_log stderr notice;/' /etc/nginx/nginx.conf && \
  adduser -D nginx && \
  rm -rf /tmp/* && \  
  apk del makedepends

VOLUME ["/var/cache/nginx"]

EXPOSE 80 443
CMD ["nginx", "-g", "daemon off;"]
