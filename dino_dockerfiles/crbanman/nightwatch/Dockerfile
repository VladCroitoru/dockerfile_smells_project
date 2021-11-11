FROM node:8-slim

#install jre
RUN set -xe \
  && echo "deb http://http.debian.net/debian jessie-backports main" >> /etc/apt/sources.list \
  && apt-get update \
  && apt-get -t jessie-backports install -y \
  openjdk-8-jre

#install application dependencies
RUN DEBIAN_FRONTEND=noninteractive \
  set -ex \
  && apt-get -y install \
#    xvfb \
    curl

#install google-chrome
RUN set -xe \
  && curl -fsSL https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
  && apt-get update \
  && apt-get install -y google-chrome-stable \
  && rm -rf /var/lib/apt/lists/*

#install nightwatch
WORKDIR /app
COPY package.json /app/
RUN npm install
COPY ./ /app/
RUN npm run postinstall
