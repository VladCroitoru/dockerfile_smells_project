FROM mhart/alpine-node:4

RUN apk add --no-cache git \
  && mkdir /app \
  && git clone --single-branch --branch "0.4.1" https://github.com/selaux/miner-dashboard.git /app \
  && mv /app/config/config.example.js /app/config/config.js \
  && cd /app \
  && npm install \
  && node_modules/.bin/grunt compile \
  && apk del git \
  && rm -rf .git \
  && rm -rf /var/cache/apk/* \
  && rm -rf /root/.npm

EXPOSE 3000
CMD node /app/app.js -c /app/config/config.js
