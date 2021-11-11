FROM node
MAINTAINER ray@wirestorm.net

ADD . /dispatcher
WORKDIR /dispatcher
RUN npm install

ENTRYPOINT ["node", "/dispatcher/index.js"]
