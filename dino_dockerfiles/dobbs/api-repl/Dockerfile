FROM ruby:2.6-alpine

RUN apk update && apk add bind-tools curl ca-certificates build-base \
 && addgroup -S -g 7777 pry \
 && adduser -s /bin/sh -u 7777 -G pry -D pry \
 && cd /home/pry \
 && su pry -c 'gem install pry faraday' \
 && su pry -c 'printf "%s\n" "Pry.pager = false" > .pryrc' \
 && su pry -c 'mkdir work'
WORKDIR /home/pry/work
USER pry

ENTRYPOINT [ "env", "pry", "-r", "faraday", "-r", "json", "-r", "yaml" ]
