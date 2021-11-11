FROM lsiobase/ubuntu:focal
#FROM openjdk:jre-slim
MAINTAINER sparklyballs, ajw107 (Alex Wood)

SHELL ["/bin/bash", "-c"]
ARG DEBIAN_FRONTEND="noninteractive"
ARG PROG_NAME="HYDRA"
ARG PROG_VER
ARG VERSION_FILE_LOCATION=/VERSION/${PROG_NAME}_VER

# set python to use utf-8 rather than ascii
ENV PYTHONIOENCODING="UTF-8"
#add extra environment settings
ENV VERSION_FILE=${VERSION_FILE_LOCATION}
ENV CONFIG="/config"
ENV APPDIRNAME="hydra"
ENV APP_ROOT="/app"
#ENV APP_OPTS="--nobrowser --config=${CONFIG}/settings.cfg --database=${CONFIG}/nzbhydra.db --logfile=${CONFIG}/nzbhydra.log"
ENV APP_OPTS="--nobrowser --datafolder ${CONFIG} --baseurl /nzbhydra"
#ENV APP_EXEC="nzbhydra2"
ENV APP_EXEC="nzbhydra2wrapper.py"
ENV APP_COMP="python"
ENV TERM=xterm-color
#ENV GITURL="https://github.com/theotherp/nzbhydra2.git"
#ENV GITBRANCH="master"

#make life easy for yourself
RUN \
    apt-get update && \
    apt-get install -y nano \
                   git \
                   curl \
                   unzip &&\
    apt-get install --no-install-recommends -y openjdk-11-jre-headless python
#RUN echo $'#!/bin/bash\nls -alF --color=auto --group-directories-first --time-style=+"%H:%M %d/%m/%Y" --block-size="\'1" $@' > /usr/bin/ll

COPY get_version /get_version
VOLUME /VERSION
RUN \
  echo "**** install hydra2 ****" && \
  if [ -z ${PROG_VER+x} ]; \
  then \
       source /get_version; \
#       PROG_VER=$(cat ${VERSION_FILE}); \
  else \
       echo "PROG_VER set by build ARG: [${PROG_VER}]"; \
  fi && \
  echo "${PROG_NAME} Ver: [${PROG_VER}]" && \
  curl -o \
  /tmp/hydra2.zip -L \
"https://github.com/theotherp/nzbhydra2/releases/download/v${PROG_VER}/nzbhydra2-${PROG_VER}-linux.zip" && \
  mkdir -p "${APP_ROOT}/${APPDIRNAME}" && \
  unzip /tmp/hydra2.zip -d "${APP_ROOT}/${APPDIRNAME}" && \
#  curl -o \
#    "${APP_ROOT}/${APPDIRNAME}/nzbhydra2wrapper.py" -L \
#	"https://raw.githubusercontent.com/theotherp/nzbhydra2/master/other/wrapper/nzbhydra2wrapper.py" && \
#  chmod +x "${APP_ROOT}/${APPDIRNAME}/nzbhydra2wrapper.py" && \
  echo "**** cleanup ****" && \
  apt-get clean && \
  rm -rf \
    /tmp/* \
    /var/lib/apt/lists/* \
    /var/tmp/*

#LABEL build_version=${HYDRA_VER}  #unfortunately variables don;t pass through layers

# copy local files
COPY root/ /
RUN chmod +x /usr/bin/ll

# ports and volumes
EXPOSE 5075
# WORKDIR /config/hydra
#VOLUME /config /downloads
VOLUME "${CONFIG}" /mnt
