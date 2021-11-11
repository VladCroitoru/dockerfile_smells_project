# You should always specify a full version here to ensure all of your developers
# are running the same version of Node.
FROM mhart/alpine-node:6
# FROM alpine

ENV NODE_VERSION 6.9.1
# The base node image sets a very verbose log level.
ENV NPM_CONFIG_LOGLEVEL info

COPY . .
RUN npm i
RUN npm run build
