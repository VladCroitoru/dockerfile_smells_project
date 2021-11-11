FROM node:latest

RUN git clone https://github.com/matrix-hacks/matrix-puppet-slack.git /app && \
  cd /app && \
  npm install

WORKDIR /app
ENTRYPOINT node index.js
