# Transmission template copied from https://github.com/odarriba/docker-transmission

FROM ubuntu:16.04
MAINTAINER agdev84

ENV DEBIAN_FRONTEND noninteractive



###########################
## PART 1 - REQUIREMENTS ##
###########################

# Basic apt-get initialization
RUN placeholder="" \
    && apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
        transmission-daemon \
        cron \
        openjdk-8-jre \
        mediainfo \
        libchromaprint-tools \
        file \
        curl \
        inotify-tools \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/*

# Install filebot
# Template taken from: https://github.com/filebot/plugins/blob/master/docker/Dockerfile
RUN placeholder="" \
    && FILEBOT_VERSION="4.7.8" \
    && FILEBOT_SHA256=c64026327cdd8b1e5e5932cef39d35e80932d527ec5c1c69b689313f7882e7b7 \
    && FILEBOT_PACKAGE=filebot_${FILEBOT_VERSION}_amd64.deb \
    && FILEBOT_BASEURL=https://downloads.sourceforge.net/project/filebot/filebot \
    && curl -L -O $FILEBOT_BASEURL/FileBot_$FILEBOT_VERSION/$FILEBOT_PACKAGE \
    && echo "$FILEBOT_SHA256 *$FILEBOT_PACKAGE" | sha256sum --check --strict \
    && dpkg -i "$FILEBOT_PACKAGE" \
    && rm "$FILEBOT_PACKAGE"


############################
## PART 2 - CONFIGURATION ##
############################

# Push required files
COPY override /override

# Setup file system
RUN placeholder="" \
    && find /override -type f -name '.git-placeholder-0bb801e065cd4749af279ecbe05d3456' -delete \
    && cp -Rf /override/. / \
    && sed -i 's/USER=debian-transmission/USER=root/g' /etc/init.d/transmission-daemon

# Default values for environment variables
ENV TR_USERNAME="transmission"
ENV TR_PASSWORD="transmission"

EXPOSE 9091 51413/tcp 51413/udp

VOLUME ["/data", "/out"]

ENTRYPOINT ["/bin/entrypoint.sh"]


