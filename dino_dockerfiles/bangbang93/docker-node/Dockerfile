FROM node:alpine

RUN printf 'https://mirrors.tuna.tsinghua.edu.cn/alpine/v3.6/main\nhttps://mirrors.tuna.tsinghua.edu.cn/alpine/v3.6/community' > /etc/apk/repositories

RUN apk update \
&& apk add build-base python

RUN npm config set registry https://registry.npm.taobao.org \
 && npm config set disturl https://npm.taobao.org/dist
