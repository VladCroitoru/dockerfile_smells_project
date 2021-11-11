ARG RESTY_IMAGE_BASE="alpine"
ARG RESTY_IMAGE_TAG="3.8"

FROM ${RESTY_IMAGE_BASE}:${RESTY_IMAGE_TAG}

LABEL maintainer="Canger <canger@dianjia.io>"

# Docker Build Arguments
ARG DYUPS_VERSION="v0.2.10"
ARG RESTY_VERSION="1.13.6.2"
ARG RESTY_OPENSSL_VERSION="1.0.2p"
ARG RESTY_PCRE_VERSION="8.42"
ARG RESTY_INSTALL_PREFIX="/opt/openresty"
ARG RESTY_CONFIG_OPTIONS="\
    --sbin-path=/usr/sbin/nginx \
    --modules-path=/usr/lib/nginx/modules \
    --conf-path=/etc/nginx/nginx.conf \
    --error-log-path=/var/log/nginx/error.log \
    --http-log-path=/var/log/nginx/access.log \
    --pid-path=/var/run/nginx.pid \
    --lock-path=/var/run/nginx.lock \
    --with-file-aio \
    --with-http_addition_module \
    --with-http_auth_request_module \
    --with-http_dav_module \
    --with-http_flv_module \
    --with-http_geoip_module=dynamic \
    --with-http_gunzip_module \
    --with-http_gzip_static_module \
    --with-http_image_filter_module=dynamic \
    --with-http_mp4_module \
    --with-http_random_index_module \
    --with-http_realip_module \
    --with-http_secure_link_module \
    --with-http_slice_module \
    --with-http_ssl_module \
    --with-http_stub_status_module \
    --with-http_sub_module \
    --with-http_v2_module \
    --with-http_xslt_module=dynamic \
    --with-ipv6 \
    --with-mail \
    --with-mail_ssl_module \
    --with-md5-asm \
    --with-pcre-jit \
    --with-sha1-asm \
    --with-stream \
    --with-stream_ssl_module \
    --with-threads \
    --add-module=ngx_http_dyups_module \
    "

# These are not intended to be user-specified
ARG _RESTY_CONFIG_DEPS="--with-openssl=/tmp/openssl-${RESTY_OPENSSL_VERSION} --with-pcre=/tmp/pcre-${RESTY_PCRE_VERSION}"


# 1) Install apk dependencies
# 2) Download and untar OpenSSL, PCRE, and OpenResty
# 3) Build OpenResty
# 4) Cleanup

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/' /etc/apk/repositories

RUN \
    addgroup -S nginx \
 && adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx nginx \
 && apk add --no-cache --virtual .build-deps \
        build-base \
        curl \
        gd-dev \
        geoip-dev \
        git \
        libxslt-dev \
        linux-headers \
        make \
        perl-dev \
        readline-dev \
        zlib-dev \
 && apk add --no-cache \
        gd \
        geoip \
        libgcc \
        libxslt \
        lua5.1 \
        lua-sec \
        lua-socket \
        zlib \
 && cd /tmp \
 && curl -fSL https://www.openssl.org/source/openssl-${RESTY_OPENSSL_VERSION}.tar.gz -o openssl-${RESTY_OPENSSL_VERSION}.tar.gz \
 && tar xzf openssl-${RESTY_OPENSSL_VERSION}.tar.gz \
 && curl -fSL https://ftp.pcre.org/pub/pcre/pcre-${RESTY_PCRE_VERSION}.tar.gz        -o pcre-${RESTY_PCRE_VERSION}.tar.gz \
 && tar xzf pcre-${RESTY_PCRE_VERSION}.tar.gz \
 && curl -fSL https://openresty.org/download/openresty-${RESTY_VERSION}.tar.gz       -o openresty-${RESTY_VERSION}.tar.gz \
 && tar xzf openresty-${RESTY_VERSION}.tar.gz \
 && cd /tmp/openresty-${RESTY_VERSION} \
 && git clone https://github.com/dianplus/ngx_http_dyups_module.git ngx_http_dyups_module \
 && cd ngx_http_dyups_module \
 && git checkout tags/${DYUPS_VERSION} \
 && cd .. \
 && ./configure --prefix=${RESTY_INSTALL_PREFIX} ${_RESTY_CONFIG_DEPS} ${RESTY_CONFIG_OPTIONS} -j$(getconf _NPROCESSORS_ONLN) \
 && make -j$(getconf _NPROCESSORS_ONLN) \
 && make install \
 && cd /tmp \
 && rm -rf \
        openssl-${RESTY_OPENSSL_VERSION} \
        openssl-${RESTY_OPENSSL_VERSION}.tar.gz \
        openresty-${RESTY_VERSION}.tar.gz openresty-${RESTY_VERSION} \
        pcre-${RESTY_PCRE_VERSION}.tar.gz pcre-${RESTY_PCRE_VERSION} \
 && apk del .build-deps \
 && ln -sf /dev/stdout /var/log/nginx/access.log \
 && ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 80

# Add additional binaries into PATH for convenience
ENV RESTY_DIR=/opt/openresty
ENV PATH=$PATH:$RESTY_DIR/luajit/bin/:$RESTY_DIR/bin/
ENV LUA_PATH=/usr/share/lua/5.1/?.lua;?.lua
ENV LUA_CPATH=/usr/lib/lua/5.1/?.so;?.so

ENTRYPOINT ["openresty", "-g", "daemon off;"]
