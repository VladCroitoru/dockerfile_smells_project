FROM alpine:3.4

ENV NGINX_VERSION 1.11.7
ENV LUAJIT_LIB /usr/local/lib
ENV LUAJIT_INC /usr/local/include/luajit-2.1

ARG VER_DOCKERIZE=v0.2.0
ARG VER_NGINX_GEOIP=1.1
ARG VER_NGINX_DEVEL_KIT=0.3.0
ARG VER_NGINX_LUA=0.10.7
ARG VER_LUAJIT=2.1.0-beta2
ARG VER_RESTY_CORE=0.1.9
ARG VER_LUAROCKS=2.4.2
COPY nginx-ssl-cert.patch /tmp/nginx-ssl-cert.patch

RUN CONFIG="\
		--prefix=/etc/nginx \
		--sbin-path=/usr/sbin/nginx \
		--modules-path=/usr/lib/nginx/modules \
		--conf-path=/etc/nginx/nginx.conf \
		--error-log-path=/var/log/nginx/error.log \
		--http-log-path=/var/log/nginx/access.log \
		--pid-path=/var/run/nginx.pid \
		--lock-path=/var/run/nginx.lock \
		--with-pcre-jit \
		--http-client-body-temp-path=/var/cache/nginx/client_temp \
		--http-proxy-temp-path=/var/cache/nginx/proxy_temp \
		--http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \
		--user=www-data \
		--group=www-data \
		--with-http_realip_module \
		--with-http_ssl_module \
		--with-http_gzip_static_module \
		--with-threads \
		--with-stream \
		--with-http_v2_module \
		--with-ld-opt='-Wl,-rpath,$LUAJIT_LIB' \
		--add-module=/tmp/ngx_http_geoip2_module-${VER_NGINX_GEOIP} \
		--add-module=/tmp/ngx_devel_kit-${VER_NGINX_DEVEL_KIT} \
		--add-module=/tmp/lua-nginx-module-${VER_NGINX_LUA} \
	" \
	&& addgroup -S www-data \
	&& adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G www-data www-data \
	&& apk add --no-cache curl \
	&& echo "downloading packages..." \
	&& apk add --no-cache --virtual .build-deps \
        libc-dev \
        make \
        openssl \
        openssl-dev \
        postgresql-dev \
        pcre-dev \
        zlib-dev \
        linux-headers \
        libmaxminddb-dev \
        build-base \
        unzip \
        luajit >/dev/null 2>&1 \
    && cd /tmp \
    && curl -fSL https://github.com/jwilder/dockerize/releases/download/${VER_DOCKERIZE}/dockerize-linux-amd64-${VER_DOCKERIZE}.tar.gz -o dockerize.tar.gz >/dev/null 2>&1 \
    && curl -fSL http://geolite.maxmind.com/download/geoip/database/GeoLite2-Country.mmdb.gz -o /etc/GeoLite2-Country.mmdb.gz >/dev/null 2>&1 \
    && curl -fSL http://luajit.org/download/LuaJIT-${VER_LUAJIT}.tar.gz -o LuaJIT-${VER_LUAJIT}.tar.gz >/dev/null 2>&1 \
    && curl -fSL https://github.com/leev/ngx_http_geoip2_module/archive/${VER_NGINX_GEOIP}.tar.gz -o ngx_http_geoip2_module.tar.gz >/dev/null 2>&1 \
    && curl -fSL https://github.com/simpl/ngx_devel_kit/archive/v${VER_NGINX_DEVEL_KIT}.tar.gz -o ngx_devel_kit.tar.gz >/dev/null 2>&1 \
    && curl -fSL https://github.com/openresty/lua-nginx-module/archive/v${VER_NGINX_LUA}.tar.gz -o lua-nginx-module.tar.gz >/dev/null 2>&1 \
    && curl -fSL https://github.com/openresty/lua-resty-core/archive/v${VER_RESTY_CORE}.tar.gz -o lua-resty-core.tar.gz >/dev/null 2>&1 \
    && curl -fSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz -o nginx.tar.gz >/dev/null 2>&1 \
    && curl -fSL http://luarocks.github.io/luarocks/releases/luarocks-${VER_LUAROCKS}.tar.gz -o luarocks.tar.gz >/dev/null 2>&1 \
    && wait \
    && gzip -d /etc/GeoLite2-Country.mmdb.gz \
    && tar -C /usr/local/bin -xzvf dockerize.tar.gz && rm dockerize.tar.gz \
    && tar -xzvf LuaJIT-${VER_LUAJIT}.tar.gz && rm LuaJIT-${VER_LUAJIT}.tar.gz \
    && tar -xzvf ngx_http_geoip2_module.tar.gz && rm ngx_http_geoip2_module.tar.gz \
    && tar -xzvf ngx_devel_kit.tar.gz && rm ngx_devel_kit.tar.gz \
    && tar -xzvf lua-nginx-module.tar.gz && rm lua-nginx-module.tar.gz \
    && tar -xzvf lua-resty-core.tar.gz && rm lua-resty-core.tar.gz \
    && tar -xzvf nginx.tar.gz && rm nginx.tar.gz \
    && tar -xzvf luarocks.tar.gz && rm luarocks.tar.gz \
    && mv /tmp/lua-resty-core-${VER_RESTY_CORE} /etc/lua-resty-core \
	&& cd /tmp/LuaJIT-${VER_LUAJIT} \
	&& make -j$(getconf _NPROCESSORS_ONLN) \
	&& make install \
	&& ln -sf /usr/local/bin/luajit-${VER_LUAJIT} /usr/local/bin/luajit \
	&& ln -sf /usr/local/bin/luajit-${VER_LUAJIT} /usr/local/bin/lua \
	&& cd /tmp/luarocks-${VER_LUAROCKS} \
	&& ./configure --with-lua-include=${LUAJIT_INC} \
	&& make -j$(getconf _NPROCESSORS_ONLN) build \
	&& make install \
	&& luarocks install pgmoon \
	&& luarocks install lbase64 \
	&& cd /tmp/nginx-$NGINX_VERSION \
	&& sed -i -e "s/\"Server: nginx\" CRLF/\"Server: pasaport.io\" CRLF/g" \
        -e "s/\"Server: \" NGINX_VER CRLF/\"Server: pasaport.io\" NGINX_VER CRLF/g" \
        src/http/ngx_http_header_filter_module.c \
	&& sed -i -e \
	    "s/static const u_char nginx\[5\] = \"\\\\x84\\\\xaa\\\\x63\\\\x55\\\\xe7\";/static const u_char nginx\[\] = \{0x0B, \'p\', \'a\', \'s\', \'a\', \'p\', \'o\', \'r\', \'t\', \'\.\', \'i\', \'o\'\};/g" \
	    src/http/v2/ngx_http_v2_filter_module.c \
	&& patch -p1 < /tmp/nginx-ssl-cert.patch && rm /tmp/nginx-ssl-cert.patch \
	&& ./configure $CONFIG \
	&& make build \
	&& make install \
	&& rm -rf /etc/nginx/html/ \
	&& mkdir /etc/nginx/conf.d/ \
	&& mkdir -p /usr/share/nginx/html/ \
	&& install -m644 html/index.html /usr/share/nginx/html/ \
	&& install -m644 html/50x.html /usr/share/nginx/html/ \
	&& ln -s ../../usr/lib/nginx/modules /etc/nginx/modules \
	&& strip /usr/sbin/nginx* \
	&& rm -rf \
	    /tmp/ngx_http_geoip2_module-${VER_NGINX_GEOIP} \
	    /tmp/ngx_devel_kit-${VER_NGINX_DEVEL_KIT} \
	    /tmp/lua-nginx-module-${VER_NGINX_LUA} \
	    /tmp/LuaJIT-${VER_LUAJIT} \
	    /tmp/nginx-${NGINX_VERSION} \
	    /tmp/luarocks-${VER_LUAROCKS} \
	&& apk add --no-cache --virtual .gettext gettext \
	&& mv /usr/bin/envsubst /tmp/ \
	\
	&& runDeps="$( \
		scanelf --needed --nobanner /usr/sbin/nginx /usr/lib/nginx/modules/*.so /tmp/envsubst \
			| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
			| sort -u \
			| xargs -r apk info --installed \
			| sort -u \
	)" \
	&& mv /tmp/envsubst /usr/local/bin/ \
    && mkdir /ssl \
	&& openssl req -subj '/CN=localhost/O=s/C=TR' -new -newkey rsa:2048 -sha256 -days 365 -nodes -x509 -keyout /ssl/server.key -out /ssl/server.crt \
	&& apk add --no-cache --virtual .nginx-rundeps $runDeps \
	&& apk del .build-deps \
	&& apk del .gettext \
	&& mkdir -p /tmp/nginx/cache \
	&& mkdir -p /tmp/nginx/tmp \
	&& ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log

COPY nginx.conf /etc/nginx/nginx.conf
COPY default.tmpl /etc/nginx/conf.d/default.tmpl
COPY snippet/* /etc/nginx/snippet/
COPY entrypoint.sh /
COPY create_gzip_files.sh /
COPY dhparam.pem /ssl/dhparam.pem

EXPOSE 80 443

ENTRYPOINT ["/entrypoint.sh"]
