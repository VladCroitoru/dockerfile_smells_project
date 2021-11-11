FROM alpine

RUN \
	apk add --no-cache git nodejs nodejs-npm \
	&& mkdir /locales \
	&& cd /srv && git clone https://github.com/cutsin/translator.git \
	# node packages
	&& cd /srv/translator && npm i \
	&& npm i --quiet --global pm2 \
	&& npm cache clean

ENTRYPOINT pm2 start /srv/translator/app.js -i 1 && /bin/sh

EXPOSE 80
