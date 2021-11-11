#SOURCE https://github.com/nginx-modules/docker-nginx-boringssl

FROM nename0/rpi-docker-boringssl:latest as boringssl-build

# Pull base image
FROM balenalib/armv7hf-alpine:latest as builder

ARG NGINX_VERSION=1.18.0
ARG GPG_KEYS=B0F4253373F8F6F510D42178520A9993A1C052F8
ARG CONFIG="\
		--prefix=/etc/nginx \
		--sbin-path=/usr/sbin/nginx \
		--modules-path=/usr/lib/nginx/modules \
		--conf-path=/etc/nginx/nginx.conf \
		--error-log-path=/var/log/nginx/error.log \
		--http-log-path=/var/log/nginx/access.log \
		--pid-path=/var/run/nginx.pid \
		--lock-path=/var/run/nginx.lock \
		--http-client-body-temp-path=/var/cache/nginx/client_temp \
		--http-proxy-temp-path=/var/cache/nginx/proxy_temp \
		--http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \
		--http-scgi-temp-path=/var/cache/nginx/scgi_temp \
		--user=nginx \
		--group=nginx \
		--with-http_ssl_module \
		--with-http_gzip_static_module \
		--with-http_auth_request_module \
		--with-threads \
		--with-compat \
		--with-file-aio \
		--with-http_v2_module \
		--with-ipv6 \
		--with-cc-opt=-I/usr/lib/boringssl/include \
		--with-ld-opt=-L/usr/lib/boringssl/lib \
		--add-dynamic-module=/usr/src/ngx_headers_more \
		--add-dynamic-module=/usr/src/ngx_brotli \
		--add-dynamic-module=/usr/src/ngx_ct \
	"

RUN [ "cross-build-start" ]

RUN apk add --no-cache --virtual .build-deps \
		autoconf \
		automake \
		bind-tools \
		binutils \
		build-base \
		ca-certificates \
		cmake \
		curl \
		gcc \
		gd-dev \
		git \
		gnupg \
		gnupg \
		go \
		libc-dev \
		libgcc \
		libstdc++ \
		libtool \
		libxslt-dev \
		linux-headers \
		make \
		pcre \
		pcre-dev \
		perl-dev \
		su-exec \
		tar \
		tzdata \
		zlib \
		zlib-dev

RUN echo "Nginx version: ${NGINX_VERSION}"
RUN curl -fSL "https://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz" -o nginx.tar.gz
RUN curl -fSL "https://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz.asc" -o nginx.tar.gz.asc
RUN export GNUPGHOME="$(mktemp -d)" \
	&& found=''; \
	for server in \
		ha.pool.sks-keyservers.net \
		hkp://keyserver.ubuntu.com:80 \
		hkp://p80.pool.sks-keyservers.net:80 \
		pgp.mit.edu \
	; do \
		echo "Fetching GPG key $GPG_KEYS from $server"; \
		gpg --keyserver "$server" --keyserver-options timeout=10 --recv-keys "$GPG_KEYS" && found=yes && break; \
	done; \
	test -z "$found" && echo >&2 "error: failed to fetch GPG key $GPG_KEYS" && exit 1; \
	gpg --batch --verify nginx.tar.gz.asc nginx.tar.gz \
	&& rm -rf "$GNUPGHOME" nginx.tar.gz.asc \
	&& mkdir -p /usr/src

RUN tar -zxC /usr/src -f nginx.tar.gz \
	&& rm nginx.tar.gz

RUN cd /usr/src/nginx-$NGINX_VERSION \
    && curl -fSL "https://raw.githubusercontent.com/nginx-modules/ngx_http_tls_dyn_size/0.5/nginx__dynamic_tls_records_1.17.7%2B.patch" -o dynamic_tls_records.patch \
	&& patch -p1 < dynamic_tls_records.patch

#	&& (git clone --depth=1 https://github.com/nginx-modules/libbrotli /usr/src/libbrotli \
#		&& cd /usr/src/libbrotli \
#		&& ./autogen.sh && ./configure && make -j$(getconf _NPROCESSORS_ONLN) && make install) \
RUN git clone --depth=1 --recurse-submodules https://github.com/google/ngx_brotli /usr/src/ngx_brotli \
	&& git clone --depth=1 https://github.com/openresty/headers-more-nginx-module /usr/src/ngx_headers_more \
	&& git clone --depth=1 https://github.com/nename0/nginx-ct /usr/src/ngx_ct

COPY --from=boringssl-build /usr/lib/boringssl /usr/lib/boringssl


RUN cd /usr/src/nginx-$NGINX_VERSION \
	&& ./configure $CONFIG \
	&& make -j$(getconf _NPROCESSORS_ONLN) \
	&& make install \
	&& rm -rf /etc/nginx/html/ \
	&& mkdir /etc/nginx/conf.d/ \
	&& mkdir -p /usr/share/nginx/html/ \
	&& install -m644 html/index.html /usr/share/nginx/html/ \
	&& install -m644 html/50x.html /usr/share/nginx/html/ \
	&& ln -s ../../usr/lib/nginx/modules /etc/nginx/modules \
	&& strip /usr/sbin/nginx* \
	&& strip /usr/lib/nginx/modules/*.so \
	&& rm -rf /usr/src/nginx-$NGINX_VERSION \
	&& rm -rf /usr/src/boringssl /usr/src/libbrotli /usr/src/ngx_* \
	&& apk del .build-deps

RUN [ "cross-build-end" ]

FROM balenalib/armv7hf-alpine:latest

RUN [ "cross-build-start" ]

RUN addgroup -S nginx \
    && adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx nginx \
    && apk add --no-cache --virtual .nginx-rundeps tini tzdata ca-certificates musl pcre zlib \
	\
	# forward request and error logs to docker log collector
	&& mkdir -p /var/log/nginx \
	&& ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log

RUN [ "cross-build-end" ]


COPY --from=builder /etc/nginx /etc/nginx
COPY --from=builder /usr/sbin/nginx /usr/sbin/
COPY --from=builder /usr/lib/nginx /usr/lib/nginx

LABEL description="nginx built from source" \
      openssl="BoringSSL"

EXPOSE 80 443

ENTRYPOINT ["/sbin/tini", "--"]
CMD ["nginx", "-g", "daemon off;"]
