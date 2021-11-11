#
# Monera-pr-bot
#
# VERSION                1.0.0

FROM node
MAINTAINER Mauro Mandracchia <info@ideabile.com>
LABEL Description="Create a pull request for GitHub" Vendor="ideabile.com" Version="1.0.1"

ENV MAIN=./

WORKDIR /
ADD ${MAIN}package.json /package.json
RUN npm install
ADD $MAIN /
RUN apt-get clean
RUN npm run compile

ENTRYPOINT ["/usr/local/bin/node", "./lib/index.js"]
