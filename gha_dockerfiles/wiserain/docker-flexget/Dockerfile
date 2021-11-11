ARG ALPINE_VER=3.13
ARG LIBTORRENT_VER=latest

FROM ghcr.io/wiserain/libtorrent:${LIBTORRENT_VER}-alpine${ALPINE_VER}-py3 AS libtorrent
FROM ghcr.io/linuxserver/baseimage-alpine:${ALPINE_VER}
LABEL maintainer="wiserain"
LABEL org.opencontainers.image.source https://github.com/wiserain/docker-flexget

ENV S6_BEHAVIOUR_IF_STAGE2_FAILS=2 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

COPY requirements.txt /defaults/

RUN \
    echo "**** install frolvlad/alpine-python3 ****" && \
	apk add --no-cache python3 && \
	if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
	python3 -m ensurepip && \
	rm -r /usr/lib/python*/ensurepip && \
	pip3 install --no-cache --upgrade pip setuptools wheel && \
	if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip; fi && \
	echo "**** install build dependencies ****" && \
	apk add --no-cache --virtual=build-deps \
		build-base \
		python3-dev \
		musl-dev \
		libffi-dev \
		openssl-dev \
		libxml2-dev \
		libxslt-dev \
		libc-dev \
		jpeg-dev \
		linux-headers && \
	pip install -r /defaults/requirements.txt && \
	apk del --purge --no-cache build-deps && \
	echo "**** install runtime dependencies ****" && \
	apk add --no-cache \
		`# libtorrent` \
		boost-python3 libstdc++ \
		`# rarfile` \
		unrar \
		`# lxml` \
		libxml2 libxslt \
		`# others` \
		jpeg \
		`#system` \
		bash bash-completion tzdata && \
	echo "**** cleanup ****" && \
	rm -rf \
		/tmp/* \
		/root/.cache

# copy libtorrent libs
COPY --from=libtorrent /libtorrent-build/usr/lib/ /usr/lib/

# copy local files
COPY root/ /

# add default volumes
VOLUME /config /data
WORKDIR /config

# expose port for flexget webui
EXPOSE 5050 5050/tcp
