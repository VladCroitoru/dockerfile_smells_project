FROM node:alpine

RUN apk add --update git \
  && yarn global add jshint mocha ionic cordova tslint typescript \
  && rm -rf ~/* \
  && rm -rf /var/cache/apk/*

ENTRYPOINT []

CMD ["ash"]
