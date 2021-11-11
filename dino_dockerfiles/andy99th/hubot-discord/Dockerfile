FROM node:latest

MAINTAINER andy99th <andy@99th.jp>

# Install hubot
RUN ln -s /usr/bin/nodejs /usr/bin/node \
 && npm install -g coffee-script \
 && npm install -g yo generator-hubot cron \
 && npm install -g node-gyp


# Create user
RUN useradd -d /hubot -m -s /bin/bash -U hubot

# Change User and Directory
USER hubot
WORKDIR /hubot

# Setup hubot
RUN yo hubot --owner="andy99th" --name="HuBot" --description="HuBot on Docker" --defaults

# Install adapter and modules
RUN npm install coffee-script@1.12.6 \
 && npm install --save time lodash \
 && npm install --save node-opus@0.2.0 opusscript@0.0.4 libsodium-wrappers@0.7.0 uws@8.14.0 \
 && npm install --save sodium \
 && npm install --save zlib-sync \
 && npm install --save erlpack@discordapp/erlpack \
 && npm install --unsafe-perm --save git+https://github.com/ciaranlangton/hubot-discord

# Install hubot tools
RUN sed -i '/hubot-heroku-keepalive/d' external-scripts.json

# Set script directory
VOLUME ["/hubot/scripts"]

# Run hubot
ENTRYPOINT ["bin/hubot"]
CMD ["-a", "discord", "--name", "'bot'"]
