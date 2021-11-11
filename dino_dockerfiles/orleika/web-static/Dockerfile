FROM alpine:3.4

MAINTAINER orleika <orleika.net@gmail.com>

ARG NGINX_VERSION=1.11.7
ARG LIBRESSL_VERSION=2.4.4
ARG GPG_LIBRESSL="A1EB 079B 8D3E B92B 4EBD  3139 663A F51B D5E4 D8D5"
ARG GPG_NGINX="B0F4 2533 73F8 F6F5 10D4  2178 520A 9993 A1C0 52F8"

RUN addgroup -S nginx \
  && adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx nginx \
  && BUILD_CORES=$(getconf _NPROCESSORS_ONLN) \
  && apk add --update --no-cache --virtual .build_dep \
  build-base \
  linux-headers \
  ca-certificates \
  automake \
  autoconf \
  git \
  tar \
  libtool \
  pcre-dev \
  zlib-dev \
  binutils \
  gnupg \
  && apk add --update --no-cache \
  pcre \
  zlib \
  libgcc \
  libstdc++ \
  openssl \
  bind-tools \
  && cd /tmp \
  && git clone https://github.com/bagder/libbrotli --depth=1 && cd libbrotli \
  && ./autogen.sh && ./configure && make -j ${BUILD_CORES} && make install \
  && cd /tmp \
  && git clone https://github.com/google/ngx_brotli --recursive \
  && git clone https://github.com/openresty/headers-more-nginx-module --depth=1 \
  && LIBRESSL_TARBALL="libressl-${LIBRESSL_VERSION}.tar.gz" \
  && wget -q http://ftp.openbsd.org/pub/OpenBSD/LibreSSL/${LIBRESSL_TARBALL} \
  && echo "Verifying ${LIBRESSL_TARBALL}..." \
  && wget -q http://ftp.openbsd.org/pub/OpenBSD/LibreSSL/${LIBRESSL_TARBALL}.asc \
  && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_LIBRESSL" \
  && gpg --batch --verify ${LIBRESSL_TARBALL}.asc ${LIBRESSL_TARBALL} \
  && tar xzf ${LIBRESSL_TARBALL} \
  && NGINX_TARBALL="nginx-${NGINX_VERSION}.tar.gz" \
  && wget -q https://nginx.org/download/${NGINX_TARBALL} \
  && echo "Verifying ${NGINX_TARBALL}..." \
  && wget -q https://nginx.org/download/${NGINX_TARBALL}.asc \
  && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_NGINX" \
  && gpg --batch --verify ${NGINX_TARBALL}.asc ${NGINX_TARBALL} \
  && tar xzf ${NGINX_TARBALL} && cd nginx-${NGINX_VERSION} \
  && ./configure \
    --prefix=/etc/nginx \
    --sbin-path=/usr/sbin/nginx \
    --conf-path=/etc/nginx/nginx.conf \
    --http-log-path=/var/log/nginx/access.log \
    --error-log-path=/var/log/nginx/error.log \
    --pid-path=/var/run/nginx.pid \
    --lock-path=/var/run/nginx.lock \
    --user=nginx \
    --group=nginx \
    --with-cc-opt='--pipe -O3 -fPIE -fstack-protector-all -Wstack-protector --param ssp-buffer-size=4 -Wformat -Werror=format-security -Wno-deprecated-declarations' \
    --with-ld-opt='-Wl,-Bsymbolic-functions -Wl,-z,relro,-z,now' \
    --with-openssl=/tmp/libressl-${LIBRESSL_VERSION} \
    --with-http_ssl_module \
    --with-http_v2_module \
    --with-http_gzip_static_module \
    --with-http_stub_status_module \
    --with-file-aio \
    --with-threads \
    --with-pcre-jit \
    --without-http_userid_module \
    --without-http_ssi_module \
    --without-http_scgi_module \
    --without-http_userid_module \
    --without-http_uwsgi_module \
    --without-http_geo_module \
    --without-http_autoindex_module \
    --without-http_map_module \
    --without-http_split_clients_module \
    --without-http_memcached_module \
    --without-http_empty_gif_module \
    --without-http_browser_module \
    --without-http_proxy_module \
    --without-http_fastcgi_module \
    --add-module=/tmp/headers-more-nginx-module \
    --add-module=/tmp/ngx_brotli \
  && make -j ${BUILD_CORES} && make install && make clean \
  && rm -rf /etc/nginx/html/ \
  && mkdir /etc/nginx/conf.d/ \
  && mkdir -p /usr/share/nginx/html/ \
  && install -m644 html/index.html /usr/share/nginx/html/ \
  && install -m644 html/50x.html /usr/share/nginx/html/ \
  && strip -s /usr/sbin/nginx \
  && apk del .build_dep \
  && rm -rf /tmp/*  /root/.gnupg

COPY nginx.conf /etc/nginx/nginx.conf
COPY vhost_http.conf /etc/nginx/conf.d/vhost_http.conf
COPY vhost_https.conf /etc/nginx/conf.d/vhost_https.conf
COPY ssl_params /etc/nginx/conf.d/ssl_params
COPY headers_params /etc/nginx/conf.d/headers_params
COPY block_bots /etc/nginx/conf.d/block_bots
COPY block_hotlink /etc/nginx/conf.d/block_hotlink
COPY block_spams /etc/nginx/conf.d/block_spams
COPY default.conf /etc/nginx/sites-enabled/default.conf

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
