FROM node:0.12

MAINTAINER SPHERE.IO Support <support@sphere.io>

WORKDIR /app

VOLUME /app/tmp

ENV APP_ENV=docker NODE_ENV=production

RUN \
  npm config set registry http://registry.npmjs.org/ && \
  npm i -g phantomjs-prebuilt

COPY ./container/files /
COPY . /app

RUN ./container/compile

EXPOSE 8888

CMD ["npm", "start"]
