FROM ruby:2.3.0

RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs

RUN mkdir /us_web
WORKDIR /us_web

ADD Gemfile /us_web/Gemfile
ADD Gemfile.lock /us_web/Gemfile.lock
RUN bundle install

ADD . /us_web

RUN bundle exec rake assets:precompile
RUN bin/rails db:migrate RAILS_ENV=development
RUN bin/rails db:seed
