FROM node:slim

WORKDIR /usr/src/app
ADD https://github.com/twhtanghk/dns-template/archive/master.tar.gz /tmp
RUN tar --strip-components=1 -xzf /tmp/master.tar.gz && \
        rm /tmp/master.tar.gz && \
	npm install
EXPOSE 1337
        
ENTRYPOINT node app.js --prod
