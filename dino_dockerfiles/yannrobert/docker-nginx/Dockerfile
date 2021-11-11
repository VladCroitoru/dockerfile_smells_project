# Custom Nginx build with the bunch of 3rd party modules

FROM dddpaul/alpine-base:2.0.2

MAINTAINER Pavel Derendyaev <dddpaul@gmail.com>

ENV NGINX_VERSION 1.9.15
ENV LANG=en_US.utf8

ADD nginx-${NGINX_VERSION}.tar.gz /tmp/
ADD ngx_devel_kit /tmp/ngx_devel_kit/
ADD lua-nginx-module /tmp/lua-nginx-module/
ADD nginx_upstream_check_module /tmp/nginx_upstream_check_module/
ADD echo-nginx-module /tmp/echo-nginx-module/

# Install Nginx
RUN apk --update add build-base openssl-dev pcre-dev zlib-dev geoip-dev luajit-dev lua5.1-iconv \
    && cd /tmp/nginx-${NGINX_VERSION} \
	&& patch -p0 < /tmp/nginx_upstream_check_module/check_1.9.2+.patch \
	&& ./configure \
	   --prefix=/usr \
	   --conf-path=/etc/nginx/nginx.conf \
	   --http-log-path=/var/log/nginx/access.log \
	   --error-log-path=/var/log/nginx/error.log \
	   --with-pcre-jit \
	   --with-ipv6 \
	   --with-http_ssl_module \
	   --with-http_v2_module \
	   --with-http_gzip_static_module \
	   --with-http_gunzip_module \
	   --with-http_realip_module \
	   --with-http_geoip_module \
	   --with-http_stub_status_module \
	   --with-http_auth_request_module \
	   --with-http_addition_module \
	   --with-http_sub_module \
	   --add-module=/tmp/ngx_devel_kit \
	   --add-module=/tmp/lua-nginx-module \
	   --add-module=/tmp/nginx_upstream_check_module \
	   --add-module=/tmp/echo-nginx-module \
	&& make && make install \
	&& mkdir -p /etc/nginx/sites-available \
	&& mkdir -p /etc/nginx/sites-enabled \
	&& mkdir -p /var/lib/nginx \
    && apk del build-base \
    && rm -rf /var/cache/apk/* \
    && rm -rf /tmp/*

# Add files. There is a script to disable IPv6 (requires privileged mode).
ADD root /
