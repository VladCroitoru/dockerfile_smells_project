FROM lsiobase/alpine
MAINTAINER TuRDMaN

# set version label
ARG BUILD_DATE
ARG VERSION
LABEL build_version="Version:- ${VERSION} Build-date:- ${BUILD_DATE}"

# install runtime packages
RUN \
 apk update --no-cache

RUN \
 apk del --no-cache py-setuptools py-pip python

RUN \
 apk add --no-cache \
	curl \
	ffmpeg \
	ffmpeg-libs \	
	wget \
	python3 && \

# set Python3 as default
 if [ -f /usr/bin/python ] && [ -f /usr/bin/python3 ]; then ln -sf /usr/bin/python3 /usr/bin/python; \
 elif [ -f /usr/bin/python3 ]; then ln -sf /usr/bin/python3 /usr/bin/python; \
 fi && \ 

# install pip
# python3 -m ensurepip && \
#	rm -r /usr/lib/python*/ensurepip && \
#	pip3 install --upgrade pip setuptools && \	

# install build packages
# apk add --no-cache --virtual=build-dependencies \
#	cmake \
#	ffmpeg-dev \
#	g++ \
#	gcc \
#	git \
#	jpeg-dev \
#	libpng-dev \
#	make \
#	openjpeg-dev \
#	python3-dev && \

# compile mp3gain
# mkdir -p \
#	/tmp/mp3gain-src && \
# curl -o \
# /tmp/mp3gain-src/mp3gain.zip -L \
#	https://sourceforge.net/projects/mp3gain/files/mp3gain/1.5.2/mp3gain-1_5_2_r2-src.zip && \
# cd /tmp/mp3gain-src && \
# unzip -qq /tmp/mp3gain-src/mp3gain.zip && \
# sed -i "s#/usr/local/bin#/usr/bin#g" /tmp/mp3gain-src/Makefile && \
# make && \
# make install && \

# compile chromaprint
# git clone https://bitbucket.org/acoustid/chromaprint.git \
#	/tmp/chromaprint && \
# cd /tmp/chromaprint && \
# cmake \
#	-DBUILD_TOOLS=ON \
#	-DCMAKE_BUILD_TYPE=Release \
#	-DCMAKE_INSTALL_PREFIX:PATH=/usr && \
# make && \
# make install && \

# set Python3 as default
 if [ -f /usr/bin/python3 ]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \

# install pip packages
 pip3 install --no-cache-dir -U \
	irs && \
#	beets \
#	beets-copyartifacts \
#	flask \
#	pillow \
#	pip && \
#	pyacoustid \
#	pylast && \		

# cleanup
# apk del --purge \
#	build-dependencies && \
 rm -rf \
	/root/.cache \
	/tmp/*

# environment settings
ENV IRSDIR="/config" \
EDITOR="nano" \
HOME="/config"

# ports and volumes
#EXPOSE 8337
VOLUME /config /downloads /music

RUN \
# apk del py-setuptools & \
# apk del py-pip & \
 apk del python && \
 apk add python3 && \ 
# set Python3 as default
 if [ -f /usr/bin/python3 ]; then ln -sf /usr/bin/python3 /usr/bin/python; fi
# copy local files
COPY root/ /
# run shell
RUN /bin/bash
