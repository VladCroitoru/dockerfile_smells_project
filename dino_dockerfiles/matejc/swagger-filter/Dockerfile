FROM node:8

WORKDIR /usr/local/app

ADD package.json /usr/local/app

RUN yarn install

ADD . /usr/local/app

ENTRYPOINT ["yarn", "start"]
