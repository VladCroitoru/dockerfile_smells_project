FROM alpine

MAINTAINER Pete Houston <contact@petehouston.com>

RUN apk update && apk upgrade

RUN apk add --no-cache bash curl wget grep sed coreutils && rm -rf /var/cache/apk/*
