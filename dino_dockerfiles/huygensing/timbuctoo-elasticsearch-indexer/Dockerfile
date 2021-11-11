FROM node:8.6.0-alpine


RUN mkdir -p /app
WORKDIR /app

COPY package.json /app
COPY yarn.lock /app
RUN yarn install

COPY tsconfig.json /app
COPY src /app/src
RUN /app/node_modules/.bin/tsc

ENV indexer_timbuctoo_graphql_endpoint=http://example.org/timbuctoo/v5/graphql
ENV indexer_elasticsearch_host=http://example.org/elasticsearch
ENV indexer_port=80

CMD node /app/dist/app.js
