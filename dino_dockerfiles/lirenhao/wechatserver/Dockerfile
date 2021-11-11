FROM node:8-alpine

ADD ./ /opt/wechatServer

RUN apk add --no-cache --virtual .build-deps \
        g++ \
        make \
        python \
    && cd /opt/wechatServer && npm i \
    && apk del .build-deps

WORKDIR /opt/wechatServer

CMD ["npm", "start"]

VOLUME ["/opt/wechatServer/config", "/opt/wechatServer/log"]
EXPOSE 3000
