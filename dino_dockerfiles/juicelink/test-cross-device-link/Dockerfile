FROM node:6.9.1

COPY package.json /tmp/prd/package.json

WORKDIR /tmp/prd
RUN npm i --production
RUN cp -R . /tmp/src
RUN ls /tmp/src
WORKDIR /tmp/src
RUN npm i
