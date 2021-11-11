FROM node:4

MAINTAINER Andi N. Dirgantara <andi.n.dirgantara@gmail.com>

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install gcc make build-essential g++ -y
RUN npm install -g node-gyp
RUN npm install -g pm2

RUN mkdir -p /app
WORKDIR /app

COPY . /app
RUN npm install

CMD [ "pm2", "start", "--no-daemon", "app.js" ]
