FROM ubuntu:14.04

MAINTAINER Lewis Liu

RUN apt-get update \
  && apt-get -y install \
    build-essential=11.6ubuntu6 \
    curl=7.35.0-1ubuntu2.2 \
    git=1:1.9.1-1 \
    python=2.7.5-5ubuntu3 \
    nodejs=0.10.25~dfsg2-2ubuntu1 \
    npm=1.3.10~dfsg-1 \
  && apt-get clean \
  && rm -rf /tmp/* /var/tmp/*

RUN npm install -g \
  n@1.2.9 \
  && npm cache clean \
  && n 0.10.35
