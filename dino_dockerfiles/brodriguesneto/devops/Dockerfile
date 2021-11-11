FROM alpine:latest
MAINTAINER Boaventura Rodrigues Neto <brodriguesneto@gmail.com>
LABEL "app"="devops"
ENV AP /opt/app
WORKDIR $AP
RUN apk update && apk upgrade && apk add ruby ruby-json ruby-bundler && rm -rf /var/cache/apk/*
ADD Gemfile $AP/
RUN bundle install
ADD devops.rb $AP/
ADD public $AP/public
CMD ["ruby", "devops.rb"]