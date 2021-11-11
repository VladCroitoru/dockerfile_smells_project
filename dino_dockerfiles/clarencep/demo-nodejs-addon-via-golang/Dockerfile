FROM golang

COPY . /usr/src/node-calculator

WORKDIR /usr/src/node-calculator

ENV NODE_VERSION 7.9.0
ENV PATH $PATH:/usr/src/nodejs/bin

RUN buildDeps="gcc libc6-dev make wget python xz-utils" \
    && apt-get update \
    && apt-get install -y $buildDeps\
    && wget -O nodejs.tar.xz "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" \
    && mkdir /usr/src/nodejs \
    && tar -xJf nodejs.tar.xz -C /usr/src/nodejs --strip-components=1 \
    && rm nodejs.tar.xz \
    && npm --registry=https://registry.npm.taobao.org install -g node-gyp \
    && make -C /usr/src/node-calculator \
    && make -C /usr/src/node-calculator test \
    && echo OK
#    && apt-get purge -y --auto-remove $buildDeps

CMD bash

