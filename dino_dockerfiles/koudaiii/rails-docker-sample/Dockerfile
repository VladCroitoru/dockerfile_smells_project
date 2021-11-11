FROM ruby:2.3.1-slim

ENV SECRET_KEY_BASE $(openssl rand -base64 32)

RUN apt-get update -qq && \
    apt-get install -y build-essential libpq-dev nodejs && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /myapp
COPY . /myapp
RUN bundle install --without test development -j4

RUN bundle exec rake assets:precompile

CMD ["script/server"]
