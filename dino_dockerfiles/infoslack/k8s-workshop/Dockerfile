FROM ruby:2.3.1

ENV RAILS_ENV production
ENV RAILS_GROUPS assets
ENV SECRET_KEY_BASE xpto

RUN apt-get update && apt-get install -y nodejs postgresql-client
ADD Gemfile* /app/
WORKDIR /app
RUN bundle install --without development test
ADD . /app
RUN bundle exec rake assets:precompile
