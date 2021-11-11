FROM debian:latest
LABEL MAINTAINER shanelau1021@gmail.com
# ENV LANG en_US.UTF-8
ENV TZ Asia/Shanghai
ENV NODE_VERSION 7.10.0

RUN apt-get -qq update && \
apt-get -qq -y install wget && \
wget -qO- http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz | tar zxv

ENV PATH /node-v$NODE_VERSION-linux-x64/bin:$PATH
RUN npm config set registry https://registry.npm.taobao.org && \
npm install -g pm2 && \
pm2 install pm2-logrotate && \
pm2 set pm2-logrotate:max_size 100M && \
pm2 set pm2-logrotate:compress true && \
pm2 set pm2-logrotate:rotateInterval '0 0 * * * *'

ENV PATH /node-v$NODE_VERSION-linux-x64/lib/node_modules/pm2/bin:$PATH

ONBUILD WORKDIR /www

ONBUILD ADD package.json /www

ONBUILD RUN npm install --registry=http://rnpm.hz.netease.com --phantomjs_cdnurl=http://npm.taobao.org/mirrors/phantomjs

ONBUILD ADD . /www

CMD ["pm2-docker", "process.yml"]