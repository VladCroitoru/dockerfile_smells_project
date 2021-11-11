FROM node:latest

RUN apt-get update && apt-get install -y \ 
	php5-cli \
    libnotify-bin \
	&& npm install -g gulp \
	&& npm install -g browserify \
	&& npm install -g forever \
	&& npm install -g yarn
