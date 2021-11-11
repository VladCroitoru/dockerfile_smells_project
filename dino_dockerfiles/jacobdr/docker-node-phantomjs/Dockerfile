FROM node:6.10.0-wheezy

ENV NODE_ENV=production

WORKDIR /home/app

COPY package.json .

RUN npm install && \
	mv node_modules/phantomjs-prebuilt/lib/phantom/bin/phantomjs /usr/bin && \
	rm -r node_modules
