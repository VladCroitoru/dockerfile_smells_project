FROM node:9.5.0-alpine

RUN apk update && apk upgrade && apk add --no-cache git openssh bash curl python grep py-pip
RUN pip install s3cmd
RUN npm -g install cross-env lerna jscrambler rimraf https://github.com/PowToon/slack-cli
RUN mkdir ~/.ssh
