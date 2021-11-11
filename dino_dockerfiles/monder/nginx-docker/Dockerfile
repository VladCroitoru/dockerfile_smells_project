FROM phusion/baseimage:0.9.18

CMD ["/sbin/my_init"]
EXPOSE 80 443

ENV NGINX_VERSION 1.11.1
ENV GPG_KEYS B0F4253373F8F6F510D42178520A9993A1C052F8
ENV CONFIG "\
--prefix=/etc/nginx \
--sbin-path=/usr/sbin/nginx \
--modules-path=/etc/nginx/modules \
--conf-path=/etc/nginx/nginx.conf \
--error-log-path=/var/log/nginx/error.log \
--http-log-path=/var/log/nginx/access.log \
--user=www-data \
--group=www-data \
--with-http_ssl_module \
--with-http_realip_module \
--with-http_sub_module \
--with-http_gunzip_module \
--with-http_gzip_static_module \
--with-http_stub_status_module \
--with-http_auth_request_module \
--with-http_geoip_module=dynamic \
--with-threads \
--with-stream \
--with-stream_ssl_module \
--with-file-aio \
--with-http_v2_module \
--add-module=/tmp/nginx_upstream_check_module \
"
ADD nginx_upstream_check_module /tmp/nginx_upstream_check_module/

RUN apt-get update \
	&& apt-get -y install build-essential libpcre3-dev zlib1g-dev libssl-dev libgeoip-dev gnupg \
\
    && curl -fSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz -o nginx.tar.gz \
    && curl -fSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz.asc  -o nginx.tar.gz.asc \
\
    && export GNUPGHOME="$(mktemp -d)" \
	&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEYS" \
	&& gpg --batch --verify nginx.tar.gz.asc nginx.tar.gz \
	&& rm -r "$GNUPGHOME" nginx.tar.gz.asc \
	&& tar -zxC /tmp -f nginx.tar.gz \
	&& rm nginx.tar.gz \
	&& cd /tmp/nginx-$NGINX_VERSION \
\
    && patch -p0 < /tmp/nginx_upstream_check_module/check_1.9.2+.patch \
\
	&& ./configure $CONFIG \
        --with-ld-opt='-Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,--as-needed' \
        --with-cc-opt='-g -O2 -fstack-protector --param=ssp-buffer-size=4 -Wformat -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2' \
    && make \
	&& make install \
\
	&& apt-get -y remove build-essential && apt-get -y autoremove \
	&& apt-get clean && rm -rf /var/cache/apt/* /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir -p /etc/confd/conf.d /etc/service/nginx /etc/service/confd

ADD confd /usr/bin/confd
ADD nginx.sh /etc/service/nginx/run
ADD confd.sh /etc/service/confd/run
ADD nginx.toml /etc/confd/conf.d/nginx.toml

