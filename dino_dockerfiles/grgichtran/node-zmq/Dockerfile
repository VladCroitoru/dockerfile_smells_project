FROM mhart/alpine-node:6

RUN apk add --no-cache --virtual .build-dependencies make gcc g++ python && \
  apk add --no-cache krb5-dev zeromq-dev

RUN npm install -g zmq
