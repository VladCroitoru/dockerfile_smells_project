FROM node:9-alpine
LABEL maintainer="f0reachARR" description="LINE<->Slack Gateway"

WORKDIR /app

COPY package.json /app/
RUN npm install
COPY . /app/

# AVOID BUG
COPY src/http_connection.js /app/node_modules/thrift/lib/nodejs/lib/thrift/http_connection.js
RUN node_modules/.bin/tsc

ENV NODE_ENV=production

VOLUME [ "/data" ]
CMD [ "npm", "start" ]