#FROM scratch
FROM ogomez/arm32v7-alpine
LABEL maintainer "KappaBull <kappa8v11@gmail.com>"
LABEL architecture="ARM32v7"

ENV DOCKER="YES"
COPY services.sh /usr/local/bin
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/community/ >> /etc/apk/repositories \
	&& set -x \
	&& apk upgrade --update \
	&& apk add \
		bash \
		'nodejs>=6.5.0' \
		nodejs-npm \
		coreutils \
		libusb \
		pcsc-lite \
		pcsc-lite-libs \
		curl \
		ca-certificates \
		util-linux \
	\
	&& apk add --virtual .build-deps \
		git \
		make \
		gcc \
		g++ \
		gzip \
		autoconf \
		automake \
		libc-dev \
		musl-dev \
		eudev-dev \
		libevent-dev \
		pcsc-lite-dev \
		libusb-dev \
		unzip \
		linux-headers \
	\
	&& npm install pm2 -g --unsafe \
	\
	&& npm install arib-b25-stream-test -g --unsafe \
	\
	# mirakurun
	&& npm install mirakurun@latest -g --unsafe --production \
	\
	# ccid
	&& cd /tmp \
	&& curl -s https://alioth.debian.org/frs/download.php/file/4205/ccid-1.4.26.tar.bz2 -o ccid-latest.tar.bz2 \
	&& tar xvf ccid-*.tar.bz2 \
	&& cd ccid-* \
	&& ./configure \
	&& make \
	&& make install \
	\
	# PX-S1UD
	&& cd /tmp \	
	&& curl -s http://plex-net.co.jp/plex/px-s1ud/PX-S1UD_driver_Ver.1.0.1.zip -o PX-S1UD_driver_Ver.1.0.1.zip \
	&& unzip PX-S1UD_driver_Ver.1.0.1.zip \
	&& cp PX-S1UD_driver_Ver.1.0.1/x64/amd64/isdbt_rio.inp /lib/firmware \
	\
	# arib25
	&& cd /tmp/ \
	&& wget http://hg.honeyplanet.jp/pt1/archive/c44e16dbb0e2.zip \
	&& unzip c44e16dbb0e2.zip \
	&& cd /tmp/pt1-c44e16dbb0e2/arib25/src \
	&& make \
	&& make install || echo "kuso" \
	\
	# recdvb
	&& cd /tmp \
	&& curl http://www13.plala.or.jp/sat/recdvb/recdvb-1.3.1.tgz -o recdvb-1.3.1.tgz \
	&& tar xvzf recdvb-1.3.1.tgz \
	&& cd recdvb-1.3.1 \
	&& ./autogen.sh \
	&& ./configure --enable-b25 \
	&& sed -i '/#include <sys\/msg.h>/d' recpt1core.h \
	&& sed -i -E 's!(#include <sys/msg.h>)!#undef _GNU_SOURCE\n#undef _BSD_SOURCE\n\1!' recpt1.c \
	&& sed -i -E 's!(#include <sys/msg.h>)!#undef _GNU_SOURCE\n#undef _BSD_SOURCE\n\1!' recpt1ctl.c \
	&& sed -i -E 's!(#include <sys/msg.h>)!#undef _GNU_SOURCE\n#undef _BSD_SOURCE\n\1!' checksignal.c \
	&& sed -i -E 's!(#include <ctype.h>)!\1\n#include <event.h>!' tssplitter_lite.c \
	&& sed -i 's#-I../driver#-I../driver -I/usr/local/include#' Makefile \
	&& make \
	&& make install \
	\
	# cleaning
	&& cd / \
	&& npm cache clean --force \
	&& apk del --purge .build-deps \
	&& rm -rf /tmp/* \
	&& rm -rf /var/cache/apk/* \
	\
	&& chmod +x /usr/local/bin/services.sh

	# forward request and error logs to docker log collector
	#&& ln -sf /dev/stdout /usr/local/var/log/mirakurun.stdout-0.log \
	#&& ln -sf /dev/stderr /usr/local/var/log/mirakurun.stderr-0.log

WORKDIR /usr/lib/node_modules/mirakurun
CMD ["/usr/local/bin/services.sh"]
EXPOSE 40772
