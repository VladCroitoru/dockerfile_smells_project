FROM node:7-alpine

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY package.json /usr/src/app

RUN npm install

COPY . /usr/src/app

RUN chmod +x ./bin/hubot

CMD ["bin/hubot", "--adapter", "slack"]
