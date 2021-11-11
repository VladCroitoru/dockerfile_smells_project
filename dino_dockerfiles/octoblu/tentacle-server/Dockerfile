FROM node:0.10
MAINTAINER Octoblu <docker@octoblu.com>

EXPOSE 1528
HEALTHCHECK CMD nc -z 127.0.0.1 1528 || exit 1

RUN apt-get update && apt-get install -y --no-install-recommends \
  netcat \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ARG NODE_ENV
ENV NODE_ENV $NODE_ENV
COPY package.json /usr/src/app/
RUN npm install
COPY . /usr/src/app

CMD [ "npm", "start" ]
