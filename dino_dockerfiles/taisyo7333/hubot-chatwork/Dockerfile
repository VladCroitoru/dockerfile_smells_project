FROM node:6.8.0
MAINTAINER Daisuke Inoue

RUN echo Asia/Tokyo > /etc/timezone
RUN dpkg-reconfigure --frontend noninteractive tzdata

RUN apt-get update -qq && apt-get install -y build-essential libpq-dev

RUN npm install -g hubot coffee-script generator-hubot yo

WORKDIR /bot-service

ADD package.json /bot-service/package.json
RUN npm install

ADD . /bot-service

EXPOSE 8080


ENTRYPOINT ["bin/hubot", "-a", "chatwork"]