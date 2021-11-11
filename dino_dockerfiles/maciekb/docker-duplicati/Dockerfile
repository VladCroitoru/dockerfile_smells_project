FROM lsiobase/mono:LTS

# set version label
ARG BUILD_DATE
ARG VERSION
LABEL build_version="Version:- ${VERSION} Build-date:- ${BUILD_DATE}"
LABEL maintainer="maciekb"

# environment settings
ENV HOME="/config"

RUN \
 echo "**** install duplicati ****" && \
 mkdir -p \
	/app/duplicati && \
 duplicati_tag=$(curl -sX GET "https://api.github.com/repos/duplicati/duplicati/releases" \
	| awk '/tag_name.*(canary|beta|release)/{print $4;exit}' FS='[""]') && \
 duplicati_zip="duplicati-${duplicati_tag#*-}.zip" && \
 curl -o \
 /tmp/duplicati.zip -L \
	"https://github.com/duplicati/duplicati/releases/download/${duplicati_tag}/${duplicati_zip}" && \
 unzip -q /tmp/duplicati.zip -d /app/duplicati && \
 echo "**** install duplicati_client ****" && \
 curl -o \
 /tmp/duplicati_client.zip -L \
	"https://github.com/Pectojin/duplicati-client/releases/download/0.4.24_beta/duplicati_client_0.4.24_gnu_linux.zip" && \
 unzip -q /tmp/duplicati_client.zip -d /app && \
 ln -s /app/duplicati_client_0.4.24_gnu_linux/duplicati_client /usr/bin/duc && \
 echo "**** install docker ****" && \
 apt-get update && \
 apt-get install --quiet --yes --no-install-recommends \
	docker.io man-db && \
 echo "**** install latest rclone beta ****" && \
 curl https://rclone.org/install.sh | bash -s beta && \
 echo "**** cleanup ****" && \
 rm -rf \
	/tmp/* \
	/var/lib/apt/lists/* \
	/var/tmp/*
 
# copy local files
COPY root/ /

# ports and volumes
EXPOSE 8200
VOLUME /data /config
