FROM lsiobase/xenial
MAINTAINER johnodon

# set version label
ARG BUILD_DATE
ARG VERSION
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:- ${BUILD_DATE}"

# environment settings
ARG DEBIAN_FRONTEND="noninteractive"
ENV HOME="/config" \
PYTHONIOENCODING=utf-8
ENV XDG_CONFIG_HOME="/config/xdg"

# install sabnzbd
RUN \
 echo "deb http://ppa.launchpad.net/jcfp/nobetas/ubuntu xenial main" >> /etc/apt/sources.list.d/sabnzbd.list && \
 echo "deb-src http://ppa.launchpad.net/jcfp/nobetas/ubuntu xenial main" >> /etc/apt/sources.list.d/sabnzbd.list && \
 echo "deb http://ppa.launchpad.net/jcfp/sab-addons/ubuntu xenial main" >> /etc/apt/sources.list.d/sabnzbd.list && \
 echo "deb-src http://ppa.launchpad.net/jcfp/sab-addons/ubuntu xenial main" >> /etc/apt/sources.list.d/sabnzbd.list && \
 apt-key adv --keyserver hkp://keyserver.ubuntu.com:11371 --recv-keys 0x98703123E0F52B2BE16D586EF13930B14BB9F05F && \
 apt-get update && \
 apt-get install -y \
	p7zip-full \
	par2-tbb \
	python-sabyenc \
	sabnzbdplus \
	unrar \
	unzip && \

# install radarr
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \
    echo "deb http://download.mono-project.com/repo/debian wheezy main" | tee /etc/apt/sources.list.d/mono-xamarin.list && \
    apt update && \
    apt install -y mono-devel mediainfo sqlite3 libmono-cil-dev wget curl && \
    apt-get -y autoremove && \
    apt-get -y clean && \
    cd /tmp && \
    wget https://github.com/Radarr/Radarr/releases/download/v0.2.0.778/Radarr.develop.0.2.0.778.linux.tar.gz && \
 mkdir -p \
	/opt/radarr && \
  tar ixzf \
 /tmp/Radarr.develop.0.2.0.778.linux.tar.gz -C \
	/opt/radarr --strip-components=1 && \	
	
# cleanup
 apt-get clean && \
 rm -rf \
	/tmp/* \
	/var/lib/apt/lists/* \
	/var/tmp/*

# add local files
COPY root/ /

# ports and volumes
EXPOSE 8080 9090 7878
VOLUME /config /downloads /incomplete-downloads /movies
