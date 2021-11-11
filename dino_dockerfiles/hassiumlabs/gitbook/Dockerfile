FROM node:slim

MAINTAINER andy@hassiumlabs.com

RUN echo "deb http://http.debian.net/debian jessie-backports main" > /etc/apt/sources.list.d/backports.list && \
	apt-get update && \
	apt-get install -y --no-install-recommends calibre curl fonts-noto git-core node-less unzip xsltproc && \
    apt-get clean && \
    apt-get autoclean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/*

RUN npm install -g browserify ebook-convert gitbook-cli uglifyjs && \
    gitbook fetch && \
    rm -rf /root/.npm /tmp/npm*

WORKDIR /srv/gitbook

VOLUME /srv/gitbook

EXPOSE 4000

CMD gitbook --version
