FROM node:7
MAINTAINER Zhang Chuan <zhangchuan@jcble.com>

ENV NODEJS_ORG_MIRROR http://npm.taobao.org/mirrors/node

COPY package.json /usr/src/app/
RUN npm config set registry https://registry.npm.taobao.org/
RUN yarn config set registry https://registry.npm.taobao.org/
RUN yarn global add omo

ENTRYPOINT ["omo"]
CMD ["--help"]
