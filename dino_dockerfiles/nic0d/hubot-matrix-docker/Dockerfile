FROM node:5
MAINTAINER nic0d

RUN apt-get update && apt-get install -y vim
RUN npm install -g coffee-script yo generator-hubot  &&  \
	useradd hubot -m 

RUN cd /home/hubot && \
	git clone https://github.com/nic0d/hubot-matrix.git && \
	cd /home/hubot/hubot-matrix && \
	npm link && \
	cd /home/hubot

USER hubot
ENV BOT_NAME "smith"
ENV BOT_OWNER "The Matrix"
ENV BOT_DESC "Agent Smith - The Matrix bot."
RUN cd /home/hubot && \
	yo hubot --owner="$BOT_OWNER" --name="$BOT_NAME" --description="$BOT_DESC" --adapter=matrix

USER root
RUN cd /home/hubot && \
	npm link hubot-matrix

USER hubot
WORKDIR /home/hubot
RUN cd /home/hubot

CMD bin/hubot -n $BOT_NAME -a matrix