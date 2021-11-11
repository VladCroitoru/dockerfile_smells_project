FROM node:10-alpine

LABEL maintainer "dfb@davidbetz.net"

WORKDIR /var/app

RUN addgroup -S recursivecall && \
    adduser -S -G recursivecall recursivecall

RUN npm install pm2 -g

COPY package.json .

RUN npm install

COPY . .

ENV PORT=3000

EXPOSE $PORT

USER recursivecall:recursivecall

CMD  ["pm2", "start", "-x", "app.js", "--name=recursivecall", "--no-daemon", "--watch"]
