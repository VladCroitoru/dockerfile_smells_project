FROM node:6

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app
RUN npm install

CMD ["./bin/hubot", "--adapter", "slack"]
