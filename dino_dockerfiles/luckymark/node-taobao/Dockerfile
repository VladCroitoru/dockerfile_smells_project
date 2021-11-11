ARG NODE_VERSION=12.18.3
FROM node:${NODE_VERSION}

RUN npm config set registry=http://registry.npm.taobao.org

RUN apk update && \
    apk add tzdata && \
    /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone
