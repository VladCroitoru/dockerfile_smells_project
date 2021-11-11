FROM google/nodejs

RUN mkdir /opt/hubot
WORKDIR /opt/hubot

RUN npm install -g hubot coffee-script yo generator-hubot

RUN useradd -ms /bin/bash node
RUN chown -R node /opt/hubot
USER node

RUN yo hubot --owner="Bot Wrangler" --name="Hubot" --description="Delightfully aware robutt" --adapter=slack --defaults --allow-root

RUN npm install hubot-slack
RUN npm install hubot-urban
RUN npm install hubot-youtube

ADD external-scripts.json /opt/hubot/external-scripts.json

# override to set proper hubot slack integration token (see slack integrations)
ENV HUBOT_SLACK_TOKEN=xxxxxxxxxxxxxxxxxxxx

CMD ["./bin/hubot", "--adapter", "slack"]
