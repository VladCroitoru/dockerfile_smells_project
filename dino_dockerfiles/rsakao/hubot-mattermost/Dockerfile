FROM node:0.12.11
MAINTAINER Reiji Sakao <reiji.sakao@gmail.com>

RUN npm install -g yo generator-hubot && useradd hubot -m -s /bin/sh

USER hubot
WORKDIR /home/hubot

ENV HUBOT_NAME matterbot
ENV HUBOT_OWNER someone
ENV HUBOT_DESCRIPTION hubot in mattermost
RUN echo no | yo hubot --adapter=mattermost --name=$HUBOT_NAME --owner=$HUBOT_OWNER --description=$HUBOT_DESCRIPTION && \
sed -i /heroku/d ./external-scripts.json

# listen endpoint
ENV MATTERMOST_ENDPOINT /hubot/incoming
# your mattermost token
ENV MATTERMOST_TOKEN oqwx9d4khjra8cw3zbis1w6fqy
# your mattermost income url
ENV MATTERMOST_INCOME_URL http://<your mattermost instance>:<port>/hooks/ncwc66caqf8d7c4gnqby1196qo
# optional: if you want to override hubot name
ENV MATTERMOST_HUBOT_USERNAME=
# optional: if you want to override your channel
ENV MATTERMOST_CHANNEL=
# optional: if you want to override hubot icon
ENV MATTERMOST_ICON_URL=
# optional: if you want to ignore self signed certificate
ENV MATTERMOST_SELFSIGNED_CERT=

EXPOSE 8080

ENTRYPOINT ["bin/hubot"]
CMD ["-a", "mattermost"]
