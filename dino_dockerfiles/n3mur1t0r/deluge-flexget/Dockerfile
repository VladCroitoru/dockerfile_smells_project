FROM lsiobase/alpine:edge

#labels
LABEL maintainer "Alexandru Mirică <n3mur1t0r@gmail.com>"

# environment variables
ENV PYTHON_EGG_CACHE="/config/plugins/.python-eggs"

RUN \
 echo "**** install build packages ****" && \
 apk add --no-cache --virtual=build-dependencies \
	g++ \
	gcc \
	libffi-dev \
	openssl-dev \
	py2-pip \
	python2-dev && \
 echo "**** install runtime packages ****" && \
 apk add --no-cache \
	ca-certificates \
	curl \
	libressl2.7-libssl \
	openssl \
	nano \
	p7zip \
	unrar \
	unzip && \
 apk add --no-cache \
	--repository http://nl.alpinelinux.org/alpine/edge/testing \
	deluge && \
 echo "**** install pip packages ****" && \
 pip install --no-cache-dir -U \
	incremental \
	pip && \
 pip install --no-cache-dir -U \
 	chardet \
	crypto \
	flexget \
	mako \
	markupsafe \
	pyopenssl \
	rarfile \
	service_identity \
	six \
	subliminal \
	twisted \
	zope.interface && \
 echo "**** cleanup ****" && \
 apk del --purge \
	build-dependencies && \
 rm -rf \
	/root/.cache

# add local files
COPY root/ /

# ports and volumes
EXPOSE 8112 58846 58946 58946/udp
VOLUME /config /downloads /flexcfg
