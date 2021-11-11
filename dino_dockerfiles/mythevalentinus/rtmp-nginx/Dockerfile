FROM alpine:latest
MAINTAINER Valentin Deville <contact@valentin-deville.eu>

ENV NGINX_VERSION 1.12.1
ENV RTMP_MODULE_VERSION 1.2.0
ENV PREFIX_NGINX "/opt/nginx/"

EXPOSE 1935
EXPOSE 80

RUN apk update && \
	apk add	\
	gcc \
	binutils-libs \
	binutils \
	gmp \
	isl \
	libgomp \
	libatomic \
	libgcc \
	openssl \
	pkgconf \
	pkgconfig \
	mpfr3 \
	mpc1 \
	libstdc++ \
	ca-certificates \
	libssh2 \
	expat \
	pcre \
	musl-dev \
	libc-dev \
	pcre-dev \
	zlib-dev \
	openssl-dev \
	unzip \
	tar \
	make \
	wget \
	apache2-utils

WORKDIR /tmp

RUN wget http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz -O nginx.tar.gz &&	\
	wget https://github.com/arut/nginx-rtmp-module/archive/v${RTMP_MODULE_VERSION}.zip -O rtmp-module.zip

RUN unzip rtmp-module.zip && \
	tar xzf nginx.tar.gz && \
	cd nginx-${NGINX_VERSION} && \
	./configure	 \
		--prefix=${PREFIX_NGINX} \
		--with-http_ssl_module \
		--add-module=../nginx-rtmp-module-${RTMP_MODULE_VERSION} &&	\
	make &&	\
	make install && \
	rm -rf /tmp/*

ADD nginx.conf ${PREFIX_NGINX}/conf/nginx.conf
ADD entrypoint.sh /root/entrypoint.sh

CMD ["sh", "/root/entrypoint.sh"]

