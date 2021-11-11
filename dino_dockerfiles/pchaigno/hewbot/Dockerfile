# hewbot
#
# VERSION               1.0
FROM node:5.12
MAINTAINER Paul Chaignon <paul.chaignon@gmail.com>

# Install ssdeep library
RUN apt-get update
RUN apt-get install -y libfuzzy-dev redis-server

ADD . /hewbot
WORKDIR /hewbot

RUN npm install

# Default adapter and name
ENV ADAPTER shell
ENV NAME hewbot

# Default environment variables in case IRC adapter is used
# User needs to define ADAPTER, NAME, HUBOT_IRC_ROOMS
# and eventually HUBOT_IRC_NICKSERV_PASSWORD
ENV HUBOT_IRC_SERVER "irc.freenode.net"
ENV HUBOT_IRC_PORT 6697
ENV HUBOT_IRC_DEBUG "true"
ENV HUBOT_IRC_USESSL "true"
ENV HUBOT_IRC_UNFLOOD "true"

ENTRYPOINT bin/hubot --adapter $HUBOT_ADAPTER --name $HUBOT_NAME
