FROM node:16-alpine

USER root

WORKDIR /app

COPY config.json .
COPY package.json .
COPY commandblock.js .
COPY .env .

RUN apk add --no-cache \
    python3 g++ make \
    && npm install -g node-gyp \
    && npm install dotenv tmi.js sleep console-stamp

CMD [ "node", "commandblock.js" ]