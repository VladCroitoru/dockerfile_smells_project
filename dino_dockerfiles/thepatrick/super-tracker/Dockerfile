FROM node:8-slim

ENV TZ=Australia/Sydney

# Install latest chrome (dev) package, so we have the dependenceis for chromium
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' \
  && apt-get update \
  && apt-get install -y \
    google-chrome-unstable \
  && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
  && echo $TZ > /etc/timezone

COPY package.json package-lock.json /app/

WORKDIR /app

RUN npm config set unsafe-perm true && npm install

COPY . /app

CMD node get.js

# node --experimental-modules