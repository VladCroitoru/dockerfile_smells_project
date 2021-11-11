FROM ubuntu:14.04

MAINTAINER Tomohisa Kusano <siomiz@gmail.com>

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-key ED8E640A \
	&& echo "deb http://ppa.launchpad.net/mc3man/trusty-media/ubuntu trusty main" \
		>> /etc/apt/sources.list \
	&& echo "deb-src http://ppa.launchpad.net/mc3man/trusty-media/ubuntu trusty main" \
		>> /etc/apt/sources.list

RUN apt-get update \
	&& DEBIAN_FRONTEND=noninteractive \
	apt-get install -y \
	autoconf \
	ffmpeg \
	git-core \
	libpng12-dev \
	libtool \
	nasm \
	nodejs-legacy \
	npm

RUN git clone https://github.com/mozilla/node-janus /opt/node-janus

WORKDIR /opt/node-janus

RUN npm install

RUN npm cache clean \
	&& apt-get purge -y autoconf git-core libpng12-dev libtool nasm \
	&& apt-get autoremove --purge -y \
	&& apt-get clean

ADD cmd.js /opt/node-janus/cmd.js

EXPOSE 55055

CMD ["node", "cmd.js"]

