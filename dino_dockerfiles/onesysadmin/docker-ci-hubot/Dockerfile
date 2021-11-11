FROM ubuntu:trusty

MAINTAINER Alex Sanz <asans@evirtualpost.com>

RUN apt-get -qq update
RUN apt-get install -y curl
# hubot dependencies
RUN apt-get install -y g++ make python-dev libexpat1-dev libicu-dev
# supervisor 3.0b2 comes with ubuntu trusty
RUN apt-get install -y supervisor
#optional (redis 2.8.4 under trusty, can be link external redis)
RUN apt-get install -y redis-server

RUN curl http://nodejs.org/dist/v0.10.28/node-v0.10.28-linux-x64.tar.gz | tar -C /usr/local/ --strip-components=1 -zx
RUN npm install -g coffee-script hubot
RUN hubot --create /hubot

WORKDIR /hubot
RUN npm install && npm install --save hubot-hipchat

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD hubot-scripts.json /hubot/hubot-scripts.json
CMD ["supervisord", "-n"]
