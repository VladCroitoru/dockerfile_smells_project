FROM node:8.7.0
LABEL  maintainer "gaku <pro.gaku@gmail.com>"
RUN npm install -g yo generator-hubot
RUN npm install hubot-slack --save
RUN adduser myhubot
RUN chown myhubot.myhubot /home/myhubot
USER myhubot
WORKDIR /home/myhubot

ADD launch.sh /launch/launch.sh

CMD bash /launch/launch.sh
