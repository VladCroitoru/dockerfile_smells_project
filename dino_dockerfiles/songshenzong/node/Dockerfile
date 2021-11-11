FROM node:alpine

RUN mkdir -p /src \
    && npm install -g webpack gulp bower \
    && apk add --update bash \
    && rm -rf /var/cache/apk/* \
    && npm install -g cnpm --registry=https://registry.npm.taobao.org

WORKDIR /src

#install nodejs dependencies
CMD cnpm install && cnpm start
