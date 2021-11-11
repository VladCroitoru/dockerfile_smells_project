FROM node:7

MAINTAINER KUN <nguyentruongthanh.dn@gmail.com>

USER root

RUN echo 'deb http://ftp.debian.org/debian jessie-backports main' >> /etc/apt/sources.list \
    && curl -sS http://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
    && apt-get update \
    && apt-get install yarn

RUN npm install --global \
    loopback-cli \
    strong-pm \
    && npm cache clear \
    && sl-pm-install

WORKDIR /usr/app
