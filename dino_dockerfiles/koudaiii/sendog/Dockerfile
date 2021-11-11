FROM ruby:2.3.1-slim

RUN bundle config --global frozen 1

WORKDIR /app
COPY sendog.rb /app/
COPY Gemfile /app/
COPY Gemfile.lock /app/

RUN bundle install -j4 --without test development --system

CMD ["bundle", "exec","ruby","sendog.rb"]
