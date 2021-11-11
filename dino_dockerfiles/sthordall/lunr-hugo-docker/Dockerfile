FROM node:7.7.2

RUN mkdir /build \
    && cd /build \
    && npm install lunr-hugo

WORKDIR /build

ADD ./package.json /build/package.json

ONBUILD ADD ./content /build/content
ONBUILD RUN npm run index
