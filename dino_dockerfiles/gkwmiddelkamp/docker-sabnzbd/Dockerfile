FROM ubuntu:bionic
MAINTAINER Gijs Middelkamp

# set version label
ARG BUILD_DATE
ARG VERSION
LABEL build_version="gkwmiddelkamp version:- ${VERSION} Build-date:- ${BUILD_DATE}"

# environment settings
ARG DEBIAN_FRONTEND="noninteractive"
ENV HOME="/config" \
PYTHONIOENCODING=utf-8 \
LANG=C.UTF-8 \
LC_ALL=C.UTF-8

# install packages
RUN \
 apt-get update && \
 apt-get install -y gnupg && \
 echo "deb http://ppa.launchpad.net/jcfp/nobetas/ubuntu bionic main" >> /etc/apt/sources.list.d/sabnzbd.list && \
 echo "deb-src http://ppa.launchpad.net/jcfp/nobetas/ubuntu bionic main" >> /etc/apt/sources.list.d/sabnzbd.list && \
 echo "deb http://ppa.launchpad.net/jcfp/sab-addons/ubuntu bionic main" >> /etc/apt/sources.list.d/sabnzbd.list && \
 echo "deb-src http://ppa.launchpad.net/jcfp/sab-addons/ubuntu bionic main" >> /etc/apt/sources.list.d/sabnzbd.list && \
 apt-key adv --keyserver hkp://keyserver.ubuntu.com:11371 --recv-keys 0x98703123E0F52B2BE16D586EF13930B14BB9F05F && \
 apt-get update && \
 apt-get install -y \
	python3 \
	p7zip-full \
	par2-tbb \
	python-sabyenc \
	sabnzbdplus \
	unrar \
	ffmpeg \
	git \
	unzip && \
# cleanup
 apt-get clean && \
 rm -rf \
	/tmp/* \
	/var/lib/apt/lists/* \
	/var/tmp/*

# add local files
COPY root/ /

RUN mkdir /scripts && git clone https://github.com/clinton-hall/nzbToMedia.git /scripts && cp /scripts/autoProcessMedia.cfg.spec /scripts/autoProcessMedia.cfg
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.6 2 && update-alternatives  --set python /usr/bin/python3.6

# ports and volumes
EXPOSE 8080 9090
VOLUME /config /downloads /incomplete-downloads

CMD ["env","LANG=C.UTF-8","LC_ALL=C.UTF-8", "/usr/bin/sabnzbdplus","--config-file","/config","--server","0.0.0.0:8080"]