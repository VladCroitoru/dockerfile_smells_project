FROM ruby:2.1.2
RUN apt-get update -qq && apt-get install -y build-essential libsqlite3-dev nodejs
RUN mkdir /app
WORKDIR /app
COPY Gemfile /app/Gemfile
COPY Gemfile.lock /app/Gemfile.lock
RUN bundle install
COPY . /app

EXPOSE 3000
VOLUME ["/app/db/data"]

CMD bundle exec unicorn -E production -p 3000

