FROM node:latest

# Install requirements and clean up after ourselves
RUN apt-get -q update \
  && apt-get -qy install git-core redis-server \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install hubot and related
RUN npm install -g hubot yo generator-hubot coffee-script hubot-slack

# Setup a user to run as
RUN adduser --disabled-password --gecos "" yeoman
USER yeoman
WORKDIR /home/yeoman

# Create hubot
RUN yo hubot --name hubot --description "Rewardle Hubot" --adapter slack --defaults
ENV NODE_PATH /home/yeoman/node_modules

# Default command to start up with
CMD bin/hubot --adapter slack
