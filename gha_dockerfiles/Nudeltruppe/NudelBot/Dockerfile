FROM node:16-buster

RUN apt update
RUN apt install -y ffmpeg zip

COPY package.json /usr/src/app/package.json

WORKDIR /usr/src/app

RUN npm install

COPY . /usr/src/app
COPY config.json /usr/src/app/config.json
COPY config /usr/src/app/config

RUN npm run tsc

ENTRYPOINT ["node", "/usr/src/app/out/index.js"]