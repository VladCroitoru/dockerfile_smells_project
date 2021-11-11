FROM lsiobase/xenial
MAINTAINER nicjo814

# set env variables
ENV DISPLAY=":0" \
	XAUTHORITY="/tmp/.docker.xauth" \
	APTLIST=" \
		libgl1-mesa-dri \
		libgl1-mesa-glx \
		lshw \
		module-init-tools \
		wget"

# install packages
RUN \
 apt-get update -q && \
 apt-get install \
	$APTLIST -qy && \

# add abc user to audio/video groups
 usermod -a -G audio,video abc && \

# cleanup
 cd / && \
 apt-get autoremove -y && \
 apt-get clean -y && \
 rm -rf \
	/var/lib/apt/lists/* \
	/var/tmp/* \
	/tmp/*

COPY root/ /
