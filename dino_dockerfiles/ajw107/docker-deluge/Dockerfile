FROM lsiobase/alpine
MAINTAINER Gonzalo Peci <davyjones@linuxserver.io>, sparklyballs

# environment variables
ENV CONFIG="/config"
ENV PYTHON_EGG_CACHE="${CONFIG}/plugins/.python-eggs"

# set version label
ARG BUILD_DATE
ARG VERSION
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:- ${BUILD_DATE}"

#make life easy for yourself
ENV TERM=xterm-color
RUN echo $'#!/bin/bash\nls -alF --color=auto --group-directories-first --time-style=+"%H:%M %d/%m/%Y" --block-size="\'1" $@' > /usr/bin/ll
RUN chmod +x /usr/bin/ll

# install runtime packages
RUN \
 apk add --no-cache \
	p7zip \
	python \
	unrar \
	unzip \
	nano \
	git && \
 apk add --no-cache \
	--repository http://nl.alpinelinux.org/alpine/edge/main \
	libressl2.4-libssl && \
 apk add --no-cache \
	--repository http://nl.alpinelinux.org/alpine/edge/testing \
	deluge && \

# install build packages
 apk add --no-cache --virtual=build-dependencies \
	g++ \
	gcc \
	libffi-dev \
	py-pip \
	python-dev && \

 apk add --no-cache --virtual=build-dependencies2 \
	--repository http://nl.alpinelinux.org/alpine/edge/main \
	libressl-dev && \

# install pip packages
 pip install --no-cache-dir -U \
	crypto \
	mako \
	markupsafe \
	pyopenssl \
	service_identity \
	six \
	twisted \
	zope.interface && \

# cleanup
 apk del --purge \
	build-dependencies \
	build-dependencies2 && \
 rm -rf \
	/root/.cache

# add local files
COPY root/ /

# ports and volumes
EXPOSE 8112 58846 58946 58946/udp
#VOLUME /config /downloads
VOLUME "${CONFIG}" /mnt
