FROM node:slim

RUN npm install --global gitbook-cli &&\
	gitbook fetch &&\
	apt-get update && apt-get install calibre -y &&\
	rm -rf /tmp/*

WORKDIR /srv/gitbook

VOLUME /srv/gitbook /srv/html

EXPOSE 4000 35729

CMD /usr/local/bin/gitbook serve
