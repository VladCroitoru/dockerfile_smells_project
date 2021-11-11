FROM node:6-slim

RUN echo "deb http://ppa.launchpad.net/git-core/ppa/ubuntu wily main" > /etc/apt/sources.list.d/git.list \
	&& apt-key adv --recv-keys --keyserver keyserver.ubuntu.com E1DF1F24 \
 	&& apt-get update \
	&& apt-get install git -y
