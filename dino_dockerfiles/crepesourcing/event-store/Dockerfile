FROM ruby:2.7.4-slim

RUN apt-get update -qq && apt-get install -y build-essential libpq-dev git && apt-get clean

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY Gemfile /usr/src/app/Gemfile
COPY Gemfile.lock /usr/src/app/Gemfile.lock
RUN bundle install

COPY app /usr/src/app/app
COPY config /usr/src/app/config
COPY db /usr/src/app/db
COPY lib /usr/src/app/lib
COPY Rakefile /usr/src/app/Rakefile

CMD ["rake"]
