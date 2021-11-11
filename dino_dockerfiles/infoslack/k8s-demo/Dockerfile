FROM ruby:2.3.1

ENV RAILS_GROUPS assets
ENV RAILS_ENV production
ENV SECRET_KEY_BASE compile

RUN apt-get update && apt-get install -y nodejs postgresql-client && mkdir /app
WORKDIR /app
ADD Gemfile* /app/
RUN bundle config build.nokogiri --use-system-libraries
RUN bundle install --without development test
ADD . /app
RUN bundle exec rake assets:precompile
