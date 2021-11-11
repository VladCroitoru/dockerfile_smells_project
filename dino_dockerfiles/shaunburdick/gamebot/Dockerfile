FROM rezzza/docker-node:latest

MAINTAINER Shaun Burdick <docker@shaunburdick.com>

ENV NODE_ENV=production \
    DICTIONARY_KEY= \
    SLACK_TOKEN= \
    SLACK_AUTO_RECONNECT= \
    STORAGE_TYPE= \
    STORAGE_CONFIG=

ADD . /usr/src/myapp

WORKDIR /usr/src/myapp

RUN ["npm", "install"]

CMD ["npm", "start"]
