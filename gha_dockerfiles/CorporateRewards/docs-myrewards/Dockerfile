FROM ruby:2.6-rc-alpine

MAINTAINER CreatekIO

WORKDIR /apidocs

COPY . ./

RUN apk add --no-cache coreutils git make g++ nodejs openssh && \
      rm -rf /var/cache/apk/* && \
      bundle install


