FROM node:latest

MAINTAINER hatch2

# create user hubot
RUN useradd hubot -m
USER hubot
WORKDIR /home/hubot

ENV NODE_PATH /home/hubot/node_modules/

# install hubot
RUN npm install hubot yo generator-hubot coffee-script hubot-slack bitbucket2slack hubot-heroku-keepalive --save

ENV PATH /home/hubot/node_modules/.bin:$PATH

# create hubot
RUN yo hubot --name coco --adapter slack --defaults

# copy files
ADD *.json ./
ADD scripts/*.coffee ./scripts/

CMD rm -f scripts/example.coffee

ENV PORT 8080
EXPOSE 8080

CMD bin/hubot --adapter slack
