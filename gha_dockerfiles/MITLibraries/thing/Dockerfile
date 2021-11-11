FROM ruby:2.3.3
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs
RUN mkdir /thing
WORKDIR /thing
ADD Gemfile /thing/Gemfile
ADD Gemfile.lock /thing/Gemfile.lock
RUN bundle install
ADD . /thing