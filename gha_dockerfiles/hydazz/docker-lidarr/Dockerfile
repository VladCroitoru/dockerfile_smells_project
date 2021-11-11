FROM vcxpz/baseimage-alpine-arr:latest

# set version label
ARG BUILD_DATE
ARG VERSION
LABEL build_version="Lidarr version:- ${VERSION} Build-date:- ${BUILD_DATE}"
LABEL maintainer="hydaz"

# environment settings
ARG BRANCH="nightly"

RUN set -xe && \
	echo "**** install build packages ****" && \
	apk add --no-cache --virtual=build-dependencies \
		jq && \
	echo "**** install runtime packages ****" && \
	apk add --no-cache \
		chromaprint && \
	if [ "$(arch)" = "x86_64" ]; then \
		ARCH="x64"; \
	elif [ "$(arch)" = "aarch64" ]; then \
		ARCH="arm64"; \
	fi && \
	echo "**** install lidarr ****" && \
	if [ -z ${VERSION} ]; then \
		VERSION=$(curl -sL "https://lidarr.servarr.com/v1/update/nightly/changes?os=linuxmusl&runtime=netcore" | jq -r '.[0].version'); \
	fi && \
	mkdir -p /app/lidarr/bin && \
	curl -o \
		/tmp/lidarr.tar.gz -L \
		"https://lidarr.servarr.com/v1/update/${BRANCH}/updatefile?version=${VERSION}&os=linuxmusl&runtime=netcore&arch=${ARCH}" && \
	tar xzf \
		/tmp/lidarr.tar.gz -C \
		/app/lidarr/bin --strip-components=1 && \
	printf "UpdateMethod=docker\nBranch=${BRANCH}\n" >/app/lidarr/package_info && \
	echo "**** cleanup ****" && \
	apk del --purge \
		build-dependencies && \
	rm -rf \
		/app/lidarr/bin/Lidarr.Update \
		/tmp/*

# copy local files
COPY root/ /

# ports and volumes
EXPOSE 8686
VOLUME /config
