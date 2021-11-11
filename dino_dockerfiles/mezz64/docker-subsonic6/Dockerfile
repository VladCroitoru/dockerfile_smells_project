FROM lsiobase/alpine:3.6
MAINTAINER mezz64

# environment variables
ENV TERM=xterm

# install packages
RUN \
 apk add --no-cache  \
	bash \
	git \
	maven \
	openjdk8

# clone source
RUN \
 git clone git://github.com/mezz64/subsonic.git /usr/src/subsonic && \
 git -C /usr/src/subsonic checkout $(git -C /usr/src/subsonic describe --tags --candidates=1 --abbrev=0) && \
 cd /usr/src/subsonic && \

# build war file
 mvn package

# copy war file to output folder
RUN \
 mkdir -p \
	/app/subsonic && \
 cp /usr/src/subsonic/subsonic-main/target/subsonic.war /app/subsonic && \
 chmod -R 777 /app/subsonic

# set version label
ARG BUILD_DATE
ARG VERSION
LABEL build_version="Mezz version:- ${VERSION} Build-date:- ${BUILD_DATE}"

# copy prebuild and war files
COPY prebuilds/ /prebuilds/
#COPY package/ /app/subsonic/

# package version settings
ARG JETTY_VER="9.3.14.v20161028"

# environment settings
ENV SUB_HOME="/app/subsonic"
ENV SUB_SETTINGS="/config"

# install build packages
RUN \
 apk add --no-cache --virtual=build-dependencies \
	curl \
	openjdk8 \
	tar && \

# install runtime packages
 apk add --no-cache \
	ffmpeg \
	flac \
	lame \
	openjdk8-jre \
	ttf-dejavu && \

# install jetty-runner
 mkdir -p \
	/tmp/jetty && \
 cp /prebuilds/* /tmp/jetty/ && \
 curl -o \
 /tmp/jetty/"jetty-runner-$JETTY_VER".jar -L \
	"https://repo.maven.apache.org/maven2/org/eclipse/jetty/jetty-runner/${JETTY_VER}/jetty-runner-{$JETTY_VER}.jar" && \
 cd /tmp/jetty && \
 install -m644 -D "jetty-runner-$JETTY_VER.jar" \
	/usr/share/java/jetty-runner.jar && \
 install -m755 -D jetty-runner /usr/bin/jetty-runner && \

# cleanup
 apk del --purge \
	build-dependencies && \
 rm -rf \
	/tmp/*

# add local files
COPY root/ /

# ports and volumes
EXPOSE 4040
VOLUME /config /media /music /playlists /podcasts
