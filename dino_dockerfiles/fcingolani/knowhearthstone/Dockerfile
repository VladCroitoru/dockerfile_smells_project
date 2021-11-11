FROM ruby:2.1-alpine

ENV CRON_UPDATE_SCHEDULE="0 0 * * *" \
    CRON_TWEET_SCHEDULE="* */6 * * *"

RUN apk add --update build-base sqlite-libs sqlite-dev \
    && mkdir -p /usr/src/app

WORKDIR /usr/src/app

# Had to disable this because bundler is failing to add support for "ruby"
# platform when running in windows -_-
# https://github.com/bundler/bundler/pull/5231
# RUN bundle config --global frozen 1
# COPY Gemfile.lock /usr/src/app/

COPY Gemfile /usr/src/app/

RUN bundle install \
    && apk del build-base sqlite-dev \
    && rm -rf /var/cache/apk/*

COPY . /usr/src/app

RUN chmod +x ./docker-cmd.sh

CMD ["./docker-cmd.sh"]
