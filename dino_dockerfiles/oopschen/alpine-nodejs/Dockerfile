# DocPad Dockerfile
FROM alpine:latest
MAINTAINER Ray Chen <linxray@gmail.com>

# Environments
ENV NODE_VERSION 4.3.0-r0

# install nodejs
ONBUILD RUN apk add -U nodejs=${NODE_VERSION}
ONBUILD RUN npm update --global npm
ONBUILD RUN rm -rf /var/cache/apk/*
ONBUILD RUN export PATH=$(npm bin -g):${PATH}
