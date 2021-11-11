FROM monokrome/node
MAINTAINER Brandon R. Stoner <monokrome@monokro.me>

RUN mkdir -p /usr/local/share/nibbler
WORKDIR /usr/local/share/nibbler

ADD hubot-scripts.json /usr/local/share/nibbler/hubot-scripts.json
ADD scripts /usr/local/share/nibbler/scripts
ADD package.json /usr/local/share/nibbler/package.json

RUN apt-get install -qq build-essential python git-core redis-server
RUN npm install

ENV HUBOT_IRC_SERVER irc.oftc.net
ENV HUBOT_IRC_ROOMS #catjugglers
ENV HUBOT_IRC_UNFLOOD true

CMD service redis-server start && node_modules/.bin/coffee node_modules/.bin/hubot -a irc --name nibbler
