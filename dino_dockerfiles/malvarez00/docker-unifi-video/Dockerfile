# Unifi-Video

FROM phusion/baseimage

LABEL maintainer="malvarez00@icloud.com"

# Environment Settings
ENV DEBIAN_FRONTEND noninteractive

RUN \
	echo "---Import the public key used by the package management system---" && \	
		apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4 && \
	echo "---Create a list file for MongoDB---" && \
	echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/4.0 multiverse" | \
		tee /etc/apt/sources.list.d/mongodb-org-4.0.list && \
	echo "---Reload local package database---" && \
	apt-get update && \
	apt-get -y dist-upgrade && \
	apt-get -y install \
		apt-utils \
		psmisc \
		lsb-release \
		binutils \
		jsvc \
		mongodb-server \
		openjdk-8-jre-headless \
		sudo \
		wget && \
	echo "---Install Unifi-Video---" && \
	curl -o \
		unifi-video.deb -L \
			"https://dl.ubnt.com/firmwares/ufv/v3.9.11/unifi-video.Ubuntu16.04_amd64.v3.9.11.deb" && \
	dpkg -i unifi-video.deb && \
	apt-get -f install && \
	echo "---Cleanup---" && \ 		
	apt-get clean && \
	rm -rf unifi-video.deb && \
	apt-get --quiet autoremove --yes && \
	apt-get --quiet --yes clean

# Data Path
VOLUME /var/lib/unifi-video

# Log Path
VOLUME /var/log/unifi-video

WORKDIR /var/lib/unifi-video

# Port - Type (TCP/UDP) - Purpose
# 7022 - TCP - SSH (NVR Side)
# 6666 - TCP - Inbound Camera Streams (NVR Side)
# 7004 - UDP - UVC-Micro Talkback (Camera Side)
# 7080 - TCP - HTTP Web UI & API (NVR Side)
# 7442 - TCP - Camera Management (NVR Side)
# 7443 - TCP - HTTPS Web UI & API (NVR Side)
# 7445 - TCP - Video over HTTP
# 7446 - TCP - Video over HTTPS
# 7447 - TCP - RTSP via the controller

EXPOSE 22 6666 7004 7080 7442 7443 7445 7446 7447

CMD ["/usr/sbin/unifi-video", "-D", "start"]
