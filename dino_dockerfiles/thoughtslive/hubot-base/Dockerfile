FROM node:4.4.3-slim

MAINTAINER "Naresh Rayapati" <naresh.rayapati@yahoo.com>

# Install CoffeeScript, Hubot
RUN \
  npm install -g coffee-script hubot yo generator-hubot && \
  rm -rf /var/lib/apt/lists/*

# Make user for Hubot
RUN groupadd -g 501 hubot && \
  useradd -m -u 501 -g 501 hubot

USER hubot
WORKDIR /home/hubot

COPY ["external-scripts.json","package.json","/home/hubot/"]
ADD bin /home/hubot/bin
ADD scripts /home/hubot/scripts

RUN npm install --silent

CMD ["/bin/sh", "-c", "bin/hubot"]
