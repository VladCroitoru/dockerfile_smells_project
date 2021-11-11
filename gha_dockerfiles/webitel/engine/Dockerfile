FROM node:12-slim
MAINTAINER Vitaly Kovalyshyn "v.kovalyshyn@webitel.com"

ENV VERSION
ENV NODE_TLS_REJECT_UNAUTHORIZED 0

COPY src /engine

WORKDIR /engine
RUN npm install

EXPOSE 10022
ENTRYPOINT ["node", "server.js"]
