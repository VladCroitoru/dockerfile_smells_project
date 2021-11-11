FROM ruby:2.2.2-slim

RUN apt-get update -qq && apt-get install -y build-essential git libpq-dev

ENV APP_HOME /app
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

ADD Gemfile* $APP_HOME/
RUN bundle install
ADD . $APP_HOME
