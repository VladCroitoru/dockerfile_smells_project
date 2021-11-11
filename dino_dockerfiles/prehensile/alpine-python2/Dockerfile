FROM janeczku/alpine-kubernetes:3.2

MAINTAINER Henry Cooke <me@prehensile.co.uk>

# update system
RUN apk update && apk upgrade

# install build essentials & python
RUN apk add python python-dev py-pip build-base && rm -rf /var/cache/apk/*
