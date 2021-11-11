FROM ruby:2-alpine

# Update and install base packages
RUN apk update && apk upgrade && apk add curl wget bash build-base

ENV PAGERDUTY_KEY=""

RUN mkdir -p /opt/diskspace

COPY diskspace/* /opt/diskspace/

WORKDIR /opt/diskspace/

RUN bundle install

ENTRYPOINT [ "bundle", "exec", "./diskspace.rb" ]
