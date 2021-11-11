FROM mhart/alpine-node:latest
MAINTAINER Drew Delianides <drew.delianides@newspring.cc>

ENV BOTDIR /opt/bot/

RUN mkdir -p /opt/bot/bin /opt/bot/scripts

ADD package.json /opt/bot/
ADD external-scripts.json /opt/bot/
ADD hubot-scripts.json /opt/bot/
ADD bin/hubot /opt/bot/bin/hubot

COPY scripts/* /opt/bot/scripts/

WORKDIR /opt/bot
RUN npm install

EXPOSE 80

ENTRYPOINT ["/opt/bot/bin/hubot"]



