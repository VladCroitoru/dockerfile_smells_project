FROM ruby:2.6.3-alpine
RUN apk add --update \
  build-base py-pip python2 python2-dev python3 python3-dev \
  && rm -rf /var/cache/apk/*

# throw errors if Gemfile has been modified since Gemfile.lock
RUN bundle config --global frozen 1
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV RACK_ENV production

COPY Gemfile Gemfile.lock /usr/src/app/
RUN bundle install --without test development --jobs 2

COPY . /usr/src/app
CMD bundle exec puma -C config/puma.rb
