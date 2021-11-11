FROM ruby:2.5
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs
RUN mkdir /dollar-exchange-rate
WORKDIR /dollar-exchange-rate
COPY Gemfile /dollar-exchange-rate/Gemfile
COPY Gemfile.lock /dollar-exchange-rate/Gemfile.lock
RUN bundle install
COPY . /dollar-exchange-rate
