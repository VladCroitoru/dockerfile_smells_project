FROM alpine:latest as builder
MAINTAINER Jessica Smith <jess@mintopia.net>

ARG OPENRESTY_VERSION=1.13.6.1
ARG NGINX_RTMP_VERSION=1.2.1


RUN	apk update		&&	\
	apk add				\
		git			\
		gcc			\
		binutils-libs		\
		binutils		\
		gmp			\
		isl			\
		libgomp			\
		libatomic		\
		libgcc			\
		openssl			\
		pkgconf			\
		pkgconfig		\
		mpfr3			\
		mpc1			\
		libstdc++		\
		ca-certificates		\
		libssh2			\
		curl			\
		expat			\
		pcre			\
		musl-dev		\
		libc-dev		\
		pcre-dev		\
		zlib-dev		\
		openssl-dev		\
		curl			\
		make            \
		perl


RUN	cd /tmp/									&&	\
	curl --remote-name https://openresty.org/download/openresty-${OPENRESTY_VERSION}.tar.gz			&&	\
	git clone https://github.com/arut/nginx-rtmp-module.git -b v${NGINX_RTMP_VERSION} 
RUN cd /tmp/ && \
	tar xzf openresty-${OPENRESTY_VERSION}.tar.gz						&&	\
	cd openresty-${OPENRESTY_VERSION}							&&	\
	./configure										\
		--prefix=/opt/openresty								\
		--with-pcre-jit \
		--with-ipv6 \
		--add-module=../nginx-rtmp-module 					&&	\
	make										&&	\
	make install

FROM alpine:latest
RUN apk update		&& \
	apk add			   \
		openssl		   \
		libstdc++	   \
		ca-certificates	   \
		pcre

COPY --from=0 /opt/openresty /opt/openresty
COPY --from=0 /tmp/nginx-rtmp-module/stat.xsl /opt/openresty/conf/stat.xsl
RUN rm /opt/openresty/nginx/conf/nginx.conf
ADD run.sh /

EXPOSE 1935
EXPOSE 8080

CMD /run.sh

