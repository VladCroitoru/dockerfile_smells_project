FROM ubuntu:14.04

MAINTAINER lingliangz@gmail.com

RUN apt-get update && apt-get install -y curl python build-essential software-properties-common
RUN apt-add-repository ppa:chris-lea/node.js
# node v12.0 doesn't support meteor
RUN apt-get update  && apt-get install -y nodejs=0.10.37-1chl1~trusty1
RUN curl https://deb.nodesource.com/setup_0.12 | bash
RUN curl https://install.meteor.com/ | sh

ADD . /srv/nyu-vote

ENV METEOR_ALLOW_SUPERUSER 1

WORKDIR /srv/nyu-vote
RUN mkdir build
RUN meteor build . && echo "1"
RUN tar -xzf nyu-vote.tar.gz
RUN (cd bundle/programs/server && npm install)

EXPOSE 3000

ENV PORT 3000

CMD node bundle/main.js
