FROM ruby:2.4-alpine
MAINTAINER Matthew Rayner <hello@rayner.io>

RUN apk add --update --no-cache build-base ruby-dev

ENV APP_HOME /app
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

COPY Gemfile Gemfile
COPY Gemfile.lock Gemfile.lock
RUN bundle install --retry 10 --jobs 4 --without test

COPY . .

EXPOSE 5000

CMD "puma"
