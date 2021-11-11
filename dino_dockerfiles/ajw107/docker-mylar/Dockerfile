FROM lsiobase/alpine.python:3.5
MAINTAINER sparklyballs, ajw107 (Alex Wood)

# set version label
ARG BUILD_DATE
ARG VERSION
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:- ${BUILD_DATE}"

# environment settings
ENV CONFIG="/config"
ENV APP_ROOT="/app"
ENV APPDIRNAME="mylar"
ENV GITURL="https://github.com/evilhero/mylar.git"
ENV GITBRANCH="development"
ENV APP_EXEC="Mylar.py"
ENV APP_OPTS="--quiet --nolaunch --datadir ${CONFIG}/mylar"
ENV APP_COMP="python"
ENV HOME="${CONFIG}"

#make life easy for yourself
ENV TERM=xterm-color
RUN apk update && apk add --no-cache nano git

# install pip packages
#TODO: I must make it auto update these on restart of the docker
RUN \
 pip install --no-cache-dir -U \
	comictagger \
	configparser \
	tzlocal && \

# cleanup
 rm -rf \
	/root/.cache \
	/tmp/*

# add local files
COPY root/ /
RUN chmod +x /usr/bin/ll

# ports and volumes
VOLUME "${CONFIG}" /mnt
EXPOSE 8090
