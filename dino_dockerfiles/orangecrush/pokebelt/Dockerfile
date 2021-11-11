FROM node
MAINTAINER Max Friederichs "max@maxfriederichs.com"

ENV PORT 3000

ADD . /root

# Install browserify
RUN npm install -g browserify

# Install deps
WORKDIR /root/public/js
RUN npm install

# Build assets
RUN browserify -t brfs app.js -o main.js

# Entrypoint for application
WORKDIR /root/server
RUN npm install
EXPOSE ${PORT}
CMD node /root/server/index.js

