FROM alpine:3.7

ENV OPENRESTY_VERSION 1.13.6.1
ENV CT_VERSION 1.3.2
ENV BROTLI_VERSION 1.3.2
ENV OPENRESTY_PREFIX /opt/verynginx/openresty
ENV NGINX_PREFIX /opt/verynginx/openresty/nginx
ENV VAR_PREFIX /var/nginx

RUN apk update \
 && apk add --no-cache \
    ca-certificates openssl \
    libpcrecpp libpcre16 libpcre32 libssl1.0 libgcc libstdc++ pcre zlib \
    bash \
 && apk add --no-cache --virtual .build-deps \
    build-base \
    linux-headers \
    openssl-dev \
    pcre-dev \
    wget \
    zlib-dev \
    curl \
    perl \
    git \
    unzip \
 && mkdir -p /root/ngx_openresty \
 && cd /root/ngx_openresty \
 && wget https://github.com/grahamedgecombe/nginx-ct/archive/v${CT_VERSION}.zip && unzip v${CT_VERSION}.zip \
 && git clone --depth=1 --recurse-submodules https://github.com/google/ngx_brotli.git \
 && curl -sSL http://openresty.org/download/openresty-${OPENRESTY_VERSION}.tar.gz | tar -xvz \
 && cd openresty-* \
 && readonly NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \
 && ./configure \
    --prefix=$OPENRESTY_PREFIX \
    --http-client-body-temp-path=$VAR_PREFIX/client_body_temp \
    --http-proxy-temp-path=$VAR_PREFIX/proxy_temp \
    --http-log-path=$VAR_PREFIX/access.log \
    --error-log-path=$VAR_PREFIX/error.log \
    --pid-path=$VAR_PREFIX/nginx.pid \
    --lock-path=$VAR_PREFIX/nginx.lock \
    --user=www-data \
    --group=www-data \
    --with-luajit \
    --with-pcre-jit \
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
    --with-threads \
    --with-stream \
    --with-stream_ssl_module \
    --with-http_slice_module \
    --with-mail \
    --with-mail_ssl_module \
    --with-file-aio \
    --with-http_v2_module \
    --with-ipv6 \
    --with-stream_realip_module \
    --without-http_ssi_module \
    --without-http_userid_module \
    --without-http_uwsgi_module \
    --with-http_stub_status_module \
    --add-module=../ngx_brotli \
    --add-module=../nginx-ct-${CT_VERSION} \
    --with-http_gzip_static_module \
    -j${NPROC} \
 && make -j${NPROC} \
 && make install \
 && ln -sf $NGINX_PREFIX/sbin/nginx /usr/local/bin/nginx \
 && ln -sf $NGINX_PREFIX/sbin/nginx /usr/local/bin/openresty \
 && ln -sf $OPENRESTY_PREFIX/bin/resty /usr/local/bin/resty \
 && ln -sf $OPENRESTY_PREFIX/luajit/bin/luajit-* $OPENRESTY_PREFIX/luajit/bin/lua \
 && ln -sf $OPENRESTY_PREFIX/luajit/bin/luajit-* /usr/local/bin/lua \
 && cd /root \
 && git clone https://github.com/camilb/VeryNginx.git \
 && rm -f $NGINX_PREFIX/conf/nginx.conf \
 && cp ./VeryNginx/nginx.conf $NGINX_PREFIX/conf/nginx.conf \
 && cp -r ./VeryNginx/verynginx /opt/verynginx \
 && rm -rf ./verynginx \
 && apk del .build-deps \
 && rm -rf /var/cache/apk/* \
 && rm -rf /root/ngx_openresty \
 && addgroup -g 1000 www-data && adduser -D -G www-data -s /bin/false -u 1000 www-data \
 && chown -R www-data:www-data /opt/verynginx  

WORKDIR $NGINX_PREFIX/

CMD ["/opt/verynginx/openresty/nginx/sbin/nginx", "-g", "daemon off; error_log /dev/stderr info;"]
