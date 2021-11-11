FROM debian:latest

RUN apt-get update
RUN apt-get install -y build-essential \
    curl \
    libpcre3 \
    libpcre3-dev \
    libxml2-dev \
    libxslt1-dev \
    tar \
    unzip \
    zlib1g-dev \
    wget
RUN rm -rf /var/lib/apt/lists/*

RUN NPS_VERSION=1.12.34.2 \
    PCRE_VERSION=8.41 \
    NGINX_VERSION=1.10.2 \
    ZLIB_VERSION=1.2.10 \
    OPENSSL_VERSION=1_1_0c \
    NGINX_LOG_PATH=/var/log/nginx \
    NGINX_USER=www-data \
    NGINX_GROUP=www-data \
    TMP_DIR=$(mktemp -d) &&\
    wget https://github.com/pagespeed/ngx_pagespeed/archive/v${NPS_VERSION}-beta.zip &&\
    unzip v${NPS_VERSION}-beta.zip -d ${TMP_DIR} &&\
    cd ${TMP_DIR}/incubator-pagespeed-ngx-${NPS_VERSION}-beta/ &&\
    psol_url=https://dl.google.com/dl/page-speed/psol/${NPS_VERSION}.tar.gz \
    [ -e scripts/format_binary_url.sh ] && psol_url=$(scripts/format_binary_url.sh PSOL_BINARY_URL) &&\
    wget ${psol_url} &&\
    tar -xzvf $(basename ${psol_url}) &&\
    cd /tmp &&\
    curl -Ls https://github.com/nginx/nginx/archive/release-${NGINX_VERSION}.tar.gz | tar -xvzf - \
        -C ${TMP_DIR} &&\
    curl -Ls ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-${PCRE_VERSION}.tar.gz | tar -xvzf - \
        -C ${TMP_DIR} &&\
    curl -Ls https://github.com/madler/zlib/archive/v${ZLIB_VERSION}.tar.gz | tar -xvzf - \
        -C ${TMP_DIR} &&\
    curl -Ls https://github.com/openssl/openssl/archive/OpenSSL_${OPENSSL_VERSION}.tar.gz | tar -xzvf - \
        -C ${TMP_DIR} &&\
    cd ${TMP_DIR}/nginx-release-${NGINX_VERSION} &&\
    sed -i -e 's/Server: nginx" CRLF/"/g' src/http/ngx_http_header_filter_module.c && sed -i -e 's/Server: " NGINX_VER CRLF/"/g' src/http/ngx_http_header_filter_module.c &&\
    ./auto/configure \
        --add-module=${TMP_DIR}/incubator-pagespeed-ngx-${NPS_VERSION}-beta \
        --conf-path=/etc/nginx/nginx.conf \
        --error-log-path=${NGINX_LOG_PATH}/error.log \
        --group=${NGINX_GROUP} \
        --http-log-path=${NGINX_LOG_PATH}/access.log \
        --lock-path=/var/lock/nginx.lock \
        --pid-path=/var/run/nginx.pid \
        --prefix=/usr/local/share/nginx \
        --sbin-path=/usr/sbin/nginx \
        --user=${NGINX_USER} \
        --with-cc-opt='-D_FORTIFY_SOURCE=2 -pie -fPIE -fstack-protector -Wformat -Wformat-security -fstack-protector -g -O1' \
        --with-ld-opt='-Wl,-z,now -Wl,-z,relro' \
        --with-http_addition_module \
        --with-http_dav_module \
        --with-http_gunzip_module \
        --with-http_gzip_static_module \
        --with-http_mp4_module \
        --with-http_realip_module \
        --with-http_secure_link_module \
        --with-http_ssl_module --with-openssl=${TMP_DIR}/openssl-OpenSSL_${OPENSSL_VERSION} \
        --with-http_sub_module \
        --with-http_sub_module \
        --with-http_xslt_module \
        --with-ipv6 \
        --with-mail \
        --with-mail_ssl_module \
        --with-pcre-jit \
        --with-pcre=${TMP_DIR}/pcre-${PCRE_VERSION} \
        --with-zlib=${TMP_DIR}/zlib-${ZLIB_VERSION} &&\
    make &&\
    make install &&\
    cd / && rm -rf ${TMP_DIR}

RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

CMD /usr/sbin/nginx
