FROM ubuntu:xenial
MAINTAINER ASCDC <ascdc@gmail.com>

RUN mkdir /script
ADD run.sh /script/run.sh

RUN DEBIAN_FRONTEND=noninteractive && \
	chmod +x /script/*.sh && \
	apt-get -qq update && \
	apt-get -y -qq dist-upgrade && \
	apt-get -y -qq install locales apt-utils && \
	locale-gen en_US.UTF-8 && \
	export LANG=en_US.UTF-8

RUN DEBIAN_FRONTEND=noninteractive && \
	apt-get -qq update && \
	apt-get -y -qq dist-upgrade && \
	apt-get -y -qq install vim curl wget git sudo python build-essential pkg-config libcairo2-dev libjpeg-dev libgif-dev && \
	mkdir -p /var/www/mirador && \
	cd /var/www/mirador && \
	curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - && \
	apt-get -qq update && \
	apt-get -y -qq install nodejs && \
	git clone https://github.com/ProjectMirador/mirador.git /var/www/mirador && \
	git checkout -b v2.6.0 && \
	npm install -g grunt-cli && \
	npm install -g bower && \
	npm install && \
	bower install --allow-root 
	
WORKDIR /var/www/mirador
ENTRYPOINT ["/script/run.sh"]