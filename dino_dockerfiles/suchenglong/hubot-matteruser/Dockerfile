FROM node:7.5.0-alpine

RUN npm install -g yo generator-hubot
RUN adduser -h /hubot -s /bin/sh -S hubot

USER  hubot
WORKDIR /hubot

RUN yo hubot --owner="owner" --name="mybot" --description="mybot" --defaults --y
RUN npm install hubot-matteruser
RUN npm install dom-js

#ENV MATTERMOST_HOST mm.com
#ENV MATTERMOST_GROUP hubot
#ENV MATTERMOST_USER hubot
#ENV MATTERMOST_PASSWORD 123456
#ENV MATTERMOST_USE_TLS true
#ENV MATTERMOST_TLS_VERIFY false
#ENV MATTERMOST_WSS_PORT 443
#ENV MATTERMOST_HTTP_PORT 443

#CMD ["bin/hubot", "--adapter", "matteruser"]
