#SOURCE https://github.com/nginx-modules/docker-nginx-boringssl

# Pull base image
FROM resin/armhf-alpine:latest as builder

RUN [ "cross-build-start" ]

RUN uname -a && cat /etc/alpine-release

RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \
  && apk update \
  && apk add --no-cache --virtual .build-deps \
		autoconf \
		automake \
		bind-tools \
		binutils \
		build-base \
		ca-certificates \
		cmake \
		curl \
		gcc \
		git \
		go \
		libc-dev \
		libgcc \
		libstdc++ \
		libtool \
		linux-headers \
		make \
		perl-dev \
		su-exec \
		tzdata

RUN git clone --depth=1 https://boringssl.googlesource.com/boringssl /usr/src/boringssl \
#		&& sed -i 's@out \([>=]\) TLS1_2_VERSION@out \1 TLS1_3_VERSION@' /usr/src/boringssl/ssl/ssl_lib.cc \
#		&& sed -i 's@ssl->version[ ]*=[ ]*TLS1_2_VERSION@ssl->version = TLS1_3_VERSION@' /usr/src/boringssl/ssl/s3_lib.cc \
#		&& sed -i 's@(SSL3_VERSION, TLS1_2_VERSION@(SSL3_VERSION, TLS1_3_VERSION@' /usr/src/boringssl/ssl/ssl_test.cc \
#		&& sed -i 's@\$shaext[ ]*=[ ]*0;@\$shaext = 1;@' /usr/src/boringssl/crypto/*/asm/*.pl \
#		&& sed -i 's@\$avx[ ]*=[ ]*[0|1];@\$avx = 2;@' /usr/src/boringssl/crypto/*/asm/*.pl \
#		&& sed -i 's@\$addx[ ]*=[ ]*0;@\$addx = 1;@' /usr/src/boringssl/crypto/*/asm/*.pl \
		&& mkdir -p /usr/src/boringssl/build /usr/lib/boringssl/lib /usr/lib/boringssl/include/ \
		&& mv /usr/src/boringssl/include/openssl /usr/lib/boringssl/include/ \
		&& ln -sf /usr/lib/boringssl/include/openssl /usr/src/boringssl/include/openssl \
		&& touch /usr/lib/boringssl/include/openssl/ssl.h \
		&& cmake -B/usr/src/boringssl/build -H/usr/src/boringssl -DCMAKE_BUILD_TYPE=RelWithDebInfo \
		&& make -C/usr/src/boringssl/build -j$(getconf _NPROCESSORS_ONLN) \
		&& cp /usr/src/boringssl/build/crypto/libcrypto.a /usr/src/boringssl/build/ssl/libssl.a /usr/lib/boringssl/lib

#	&& rm -rf /usr/src/boringssl \
#	&& apk del .build-deps

RUN [ "cross-build-end" ]

FROM scratch

COPY --from=builder /usr/lib/boringssl /usr/lib/boringssl

LABEL description="BoringSSL for raspberrypi" \
      openssl="BoringSSL"

