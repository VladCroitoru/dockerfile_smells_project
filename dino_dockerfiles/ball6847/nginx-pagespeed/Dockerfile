FROM ubuntu:16.04
MAINTAINER ball6847@gmail.com

# Version
ENV NGINX_VERSION 1.9.14
ENV NPS_VERSION 1.11.33.0
ENV TERM xterm-256color

RUN BUILD_DEPS="build-essential git unzip automake gcc make pkg-config libtool g++" && \
    sed -i 's/archive./sg.archive./g' /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y $BUILD_DEPS zlib1g-dev libpcre3-dev libssl-dev wget libfl-dev bison libbison-dev libyajl-dev liblmdb-dev libcurl4-openssl-dev libgeoip-dev libxml2-dev flex && \
    cd /usr/src && git clone https://github.com/SpiderLabs/ModSecurity && \
    cd ModSecurity/ && git checkout -b v3/master origin/v3/master && git submodule init && git submodule update && \
    cd /usr/src && git clone https://github.com/SpiderLabs/ModSecurity-nginx.git && \
    git clone https://github.com/SpiderLabs/owasp-modsecurity-crs.git && \
    wget http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz && \
    tar -xvzf nginx-${NGINX_VERSION}.tar.gz && \
    wget https://github.com/pagespeed/ngx_pagespeed/archive/release-${NPS_VERSION}-beta.zip -O release-${NPS_VERSION}-beta.zip && \
    unzip release-${NPS_VERSION}-beta.zip && \
    cd ngx_pagespeed-release-${NPS_VERSION}-beta/ && \
    wget https://dl.google.com/dl/page-speed/psol/${NPS_VERSION}.tar.gz && \
    tar -xzvf ${NPS_VERSION}.tar.gz && \
    cd /usr/src/ModSecurity && ./build.sh && ./configure && make && make install && \
    cd /usr/src/nginx-${NGINX_VERSION}/ && \
    ./configure \
      --prefix=/var/lib/nginx \
      --sbin-path=/usr/sbin/nginx \
      --conf-path=/etc/nginx/nginx.conf \
      --pid-path=/run/nginx/nginx.pid \
      --lock-path=/run/nginx/nginx.lock \
      --http-client-body-temp-path=/var/cache/nginx/client_body \
      --http-proxy-temp-path=/var/cache/nginx/proxy \
      --http-fastcgi-temp-path=/var/cache/nginx/fastcgi \
      --http-uwsgi-temp-path=/var/cache/nginx/uwsgi \
      --http-scgi-temp-path=/var/cache/nginx/scgi \
      --user=www-data \
      --group=www-data \
      --with-ipv6 \
      --with-file-aio \
      --with-pcre-jit \
      --with-http_dav_module \
      --with-http_ssl_module \
      --with-http_stub_status_module \
      --with-http_gzip_static_module \
      --with-http_v2_module \
      --with-http_auth_request_module \
      --add-module=/usr/src/ngx_pagespeed-release-${NPS_VERSION}-beta \
      --add-module=/usr/src/ModSecurity-nginx && \
    make && \
    make install && \
    mkdir -p /etc/nginx/conf && \
    cat /usr/src/owasp-modsecurity-crs/crs-setup.conf.example /usr/src/owasp-modsecurity-crs/rules/*.conf >> /etc/nginx/conf/modsecurity.conf && \
    cp /usr/src/owasp-modsecurity-crs/rules/*.data /etc/nginx/conf/ && \
    apt-get purge -y --auto-remove $BUILD_DEPS && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /usr/src/*

ADD conf/* /etc/nginx/
ADD www/ /var/www/
ADD entrypoint.sh /entrypoint.sh

VOLUME ["/var/cache/nginx", "/var/cache/ngx_pagespeed", "/var/www"]

WORKDIR /etc/nginx

EXPOSE 80 443

ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
