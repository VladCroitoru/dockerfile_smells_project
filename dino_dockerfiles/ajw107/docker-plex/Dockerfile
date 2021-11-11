FROM lsiobase/xenial
MAINTAINER Stian Larsen, sparklyballs, ajw107 (Alex Wood)

# package version
ENV PLEX_INSTALL="https://plex.tv/downloads/latest/1?channel=8&build=linux-ubuntu-x86_64&distro=ubuntu"

# global environment settings
ENV DEBIAN_FRONTEND="noninteractive"
ENV CONFIG="/config"
ENV HOME="${CONFIG}"
ENV PLEX_DOWNLOAD="https://downloads.plex.tv/plex-media-server"

#make life easy for yourself
ENV TERM=xterm-color
#it works in alpine images, but not ubuntu for some reason
#so just copying the file over instead
#RUN echo $'#!/bin/bash\nls -alF --color=auto --group-directories-first --time-style=+"%H:%M %d/%m/%Y" --block-size="\'1" $@' > /usr/bin/ll
#RUN chmod +x /usr/bin/ll

# install packages
RUN \
 apt-get update && \
 apt-get install -y \
	avahi-daemon \
	dbus \
	wget \
	nano \
	git && \

# install plex
 curl -o \
	/tmp/plexmediaserver.deb -L \
	"${PLEX_INSTALL}" && \
 dpkg -i /tmp/plexmediaserver.deb && \

# cleanup
 apt-get clean && \
 rm -rf \
	/etc/default/plexmediaserver \
	/tmp/* \
	/var/lib/apt/lists/* \
	/var/tmp/*

# add local files
COPY root/ /
RUN chmod +x /usr/bin/ll

# ports and volumes
EXPOSE 32400 32400/udp 32469 32469/udp 5353/udp 1900/udp
VOLUME "${CONFIG}" /transcode
