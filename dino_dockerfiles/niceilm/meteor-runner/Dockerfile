FROM node:4.4.7-slim

MAINTAINER flynn <niceilm@naver.com>

ENV PORT=3000
EXPOSE 3000
VOLUME /bundle
RUN ln -sf /usr/local/bin/node /usr/local/bin/nodejs

WORKDIR /bundle
CMD eval `cat /bundle/env.list` nodejs main.js