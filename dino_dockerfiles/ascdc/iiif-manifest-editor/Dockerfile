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
	apt-get -y -qq install vim curl wget git python build-essential && \
	mkdir -p /var/www/iiif-manifest-editor && \
	curl -o- https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash && \
	export NVM_DIR="/root/.nvm" && \
	[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" && \
	git clone https://github.com/bodleian/iiif-manifest-editor.git /var/www/iiif-manifest-editor && \
	cd /var/www/iiif-manifest-editor && \
	nvm install v8.1.4 && \
	nvm use v8.1.4 && \
	npm config set unsafe-perm true && \
	npm install -g node-sass && \
	npm install
	
WORKDIR /var/www/iiif-manifest-editor
ENTRYPOINT ["/script/run.sh"]
