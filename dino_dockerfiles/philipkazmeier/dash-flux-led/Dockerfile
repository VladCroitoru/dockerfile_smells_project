FROM node:alpine

WORKDIR /home/app

# Install dependencies
COPY package.json .
RUN apk --update --no-cache add libpcap-dev python \
	&& apk --update --no-cache --virtual build-dependencies add git make g++ \
	&& npm install \
	&& apk del build-dependencies \
	&& rm -rf /var/cache/apk/* 

# Run app.js on startup of the container
COPY app.js .
CMD npm start