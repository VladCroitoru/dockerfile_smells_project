FROM mhart/alpine-node:4.1
MAINTAINER Andreas Krüger

RUN apk add --update nodejs
RUN npm install -g kamailio-etcd-dispatcher

ENTRYPOINT ["etcd-dispatcher"]
