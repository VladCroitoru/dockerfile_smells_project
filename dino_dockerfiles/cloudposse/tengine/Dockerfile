FROM ubuntu:14.04

MAINTAINER Erik Osterman <e@osterman.com>

ENV NGINX_VERSION tengine-2.1.0

ENV   DEBIAN_FRONTEND noninteractive
ENV   LANGUAGE en_US.UTF-8
ENV   LANG en_US.UTF-8
ENV   LC_ALL en_US.UTF-8

# Configure timezone and locale
RUN locale-gen $LANGUAGE && \
    dpkg-reconfigure locales

WORKDIR /usr/src/

ADD https://github.com/alibaba/tengine/archive/${NGINX_VERSION}.tar.gz tengine.tar.gz

# https://github.com/alibaba/tengine/blob/master/auto/options
# https://travis-ci.org/alibaba/tengine/jobs/32304924

RUN apt-get update && \
    apt-get -y install libssl-dev \
                       libpcre3-dev \
                       zlib1g-dev \
                       libgeoip-dev \
                       libxslt1-dev \
                       libgd2-dev \
                       build-essential \
                       libc6 \
                       libexpat1 \
                       libgd2-xpm-dev \
                       libgeoip1 \
                       libgeoip-dev \
                       libpam0g \
                       libssl1.0.0 \
                       libxml2 \
                       libxslt1.1 \
                       zlib1g \
                       openssl \
                       liblua5.1-0-dev \
                       lua5.1 \
                       libgd2-xpm-dev \
                       libgeoip-dev \
                       libxslt1-dev \
                       libpcre++0 \
                       libpcre++-dev \
                       libperl-dev \
                       wget \
                       curl && \
    tar -zxvf tengine.tar.gz && \
    cd tengine-${NGINX_VERSION} && \
    ./configure \
        --enable-mods-static=all \
        --user=www-data \
        --group=www-data \
        --prefix=/usr/share/nginx \
        --conf-path=/etc/nginx/nginx.conf \
        --lock-path=/var/lock/nginx.lock \
        --pid-path=/run/nginx.pid \
        --http-client-body-temp-path=/var/lib/nginx/body \
        --http-fastcgi-temp-path=/var/lib/nginx/fastcgi \
        --http-proxy-temp-path=/var/lib/nginx/proxy \
        --http-scgi-temp-path=/var/lib/nginx/scgi \
        --http-uwsgi-temp-path=/var/lib/nginx/uwsgi \
        --with-http_ssl_module \
        --with-http_gzip_static_module \
        --with-http_gunzip_module \
        --with-md5=/usr/include/openssl \
        --with-sha1-asm \
        --with-md5-asm \
        --with-http_auth_request_module \
        --with-http_image_filter_module \
        --with-http_addition_module \
        --with-http_dav_module \
        --with-http_realip_module \
        --with-http_spdy_module \
        --with-http_ssl_module \
        --with-http_stub_status_module \
        --with-http_sub_module \
        --with-http_xslt_module \
        --with-http_upstream_ip_hash_module=shared \
        --with-http_upstream_least_conn_module=shared \
        --with-http_upstream_session_sticky_module=shared \
        --with-http_map_module=shared \
        --with-http_user_agent_module=shared \
        --with-http_mp4_module \
        --with-http_split_clients_module=shared \
        --with-http_access_module=shared \
        --with-http_user_agent_module=shared \
        --with-http_degradation_module \
        --with-http_upstream_check_module \
        --with-http_upstream_consistent_hash_module \
        --with-ipv6 \
        --with-file-aio \
        --with-mail \
        --with-mail_ssl_module \
        --with-pcre \
        --with-pcre-jit \
        --prefix=/etc/nginx \
        --with-debug \
        --http-log-path=/var/log/nginx/access.log \
        --error-log-path=/var/log/nginx/error.log \
        --sbin-path=/usr/sbin/nginx && \
    make && \
    make install && \
    mkdir /var/cache/nginx && \
    mkdir /var/ngx_pagespeed_cache && \
    mkdir /var/log/pagespeed && \
    mkdir /etc/nginx/conf.d && \
    mkdir -p /etc/nginx/sites-available && \
    mkdir -p /etc/nginx/sites-enabled && \
    mkdir -p /var/lib/nginx/body && \
    chown -R www-data:www-data /var/cache/nginx && \
    chown -R www-data:www-data /var/ngx_pagespeed_cache && \
    chown -R www-data:www-data /var/log/nginx && \
    chown -R www-data:www-data /var/log/pagespeed && \
    chown -R www-data:www-data /etc/nginx/sites-available && \
    chown -R www-data:www-data /etc/nginx/sites-enabled && \
    chown -R www-data:www-data /var/lib/nginx/body && \
    apt-get -y remove build-essential && \
    dpkg --get-selections | awk '{print $1}'|cut -d: -f1|grep -- '-dev$' | xargs apt-get remove -y && \
    rm -rf /usr/src && \
    apt-get clean all && \
    rm -rf /tmp/* && \
    ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log

ADD nginx.conf /etc/nginx/nginx.conf

ADD html/ /etc/nginx/html/


VOLUME ["/var/log/nginx"]
VOLUME ["/var/cache/nginx"]

WORKDIR /etc/nginx

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]

