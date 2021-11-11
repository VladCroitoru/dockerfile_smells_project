FROM node:9-alpine

RUN npm install -g express socket.io socket.io-redis

RUN \
  apk add --no-cache bash python py-pip unzip && \
	pip install awscli 

ENV NODE_PATH /usr/local/lib/node_modules
