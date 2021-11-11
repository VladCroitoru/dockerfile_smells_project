FROM lsiobase/alpine:3.6
MAINTAINER epatch

# set version label
ARG BUILD_DATE
ARG VERSION
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:- ${BUILD_DATE}"

# install build packages
RUN \
 apk add --no-cache --virtual=build-dependencies \
	cmake \
	ffmpeg-dev \
	g++ \
	gcc \
	git \
	jpeg-dev \
	libpng-dev \
	make \
	openjpeg-dev \
	python2-dev \
	binutils-libs \
	binutils \
	build-base \
	libgcc \
	make \
	pkgconf \
	pkgconfig \
	openssl \
	openssl-dev \
	ca-certificates \
	pcre \
	musl-dev \
	libc-dev \
	pcre-dev \
	zlib-dev \
	yasm-dev \
	lame-dev \
	libogg-dev \
	libvpx-dev \
	libvorbis-dev \
	freetype-dev \
	libtheora-dev \
	opus-dev && \

# install runtime packages
 apk add --no-cache \
	curl \
	expat \
	gdbm \
	gst-plugins-good1 \
	gstreamer1 \
	jpeg \
	lame \
	libffi \
	libpng \
	nano \
	openjpeg \
	py2-gobject3 \
	py2-pip \
	python2 \
	sqlite-libs \
	tar \
	wget \
	nasm \
	x264-dev \
	x265-dev \
	libwebp-dev \
	libass-dev \
	libcrypto1.0 \
	libssl1.0 && \
	
# add repository for fdk-aac-dev
 echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories && \

# install chromaprint and fdk-aac-dev packages
 apk add --update --no-cache \
 chromaprint \
 fdk-aac-dev && \

# compile ffmpeg
 cd /tmp && wget http://ffmpeg.org/releases/ffmpeg-3.3.2.tar.gz && \
 tar zxf ffmpeg-3.3.2.tar.gz  && \
 cd /tmp/ffmpeg-3.3.2 && \
 ./configure \
 --enable-version3 \
 --enable-gpl \
 --enable-nonfree \
 --enable-small \
 --enable-libmp3lame \
 --enable-libx264 \
 --enable-libx265 \
 --enable-libvpx \
 --enable-libtheora \
 --enable-libvorbis \
 --enable-libopus \
 --enable-libfdk-aac \
 --enable-libass \
 --enable-libwebp \
 --enable-postproc \
 --enable-avresample \
 --enable-libfreetype \
 --enable-openssl \
 --disable-debug && \
 make && \
 make install && \
 
# compile mp3gain
 mkdir -p \
	/tmp/mp3gain-src && \
 curl -o \
 /tmp/mp3gain-src/mp3gain.zip -L \
	https://sourceforge.net/projects/mp3gain/files/mp3gain/1.5.2/mp3gain-1_5_2_r2-src.zip && \
 cd /tmp/mp3gain-src && \
 unzip -qq /tmp/mp3gain-src/mp3gain.zip && \
 sed -i "s#/usr/local/bin#/usr/bin#g" /tmp/mp3gain-src/Makefile && \
 make && \
 make install && \

# install pip packages
 pip install --no-cache-dir -U \
	beets \
	beets-copyartifacts \
	flask \
	pillow \
	pip \
	pyacoustid \
	discogs-client \
	pylast \
	unidecode && \

# cleanup
 apk del --purge \
	build-dependencies && \
 rm -rf \
	/root/.cache \
	/tmp/*

# environment settings
ENV BEETSDIR="/config" \
EDITOR="nano" \
HOME="/config"

# copy local files
COPY root/ /

# ports and volumes
EXPOSE 8337
VOLUME /config /downloads /transcoded /music
