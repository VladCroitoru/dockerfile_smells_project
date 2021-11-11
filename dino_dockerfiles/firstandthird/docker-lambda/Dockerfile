FROM mhart/alpine-node:0.10

RUN mkdir /lambda && \
  cd /lambda && \
  npm install aws-sdk

ADD runner.js /lambda/runner.js

WORKDIR /lambda/function

ENTRYPOINT ["node", "/lambda/runner.js"]
