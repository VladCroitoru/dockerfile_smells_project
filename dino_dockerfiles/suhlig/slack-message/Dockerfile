FROM ruby:alpine
LABEL maintainer "Steffen Uhlig <steffen@familie-uhlig.net>"

RUN	apk add --no-cache ca-certificates

RUN	set -x \
  && apk add --no-cache --virtual .build-deps \
  build-base

RUN mkdir /app
ADD . /app
WORKDIR /app

RUN	set -x \
  && bundle install \
  && apk del .build-deps

ENTRYPOINT ["bundle", "exec", "exe/slack-message"]
