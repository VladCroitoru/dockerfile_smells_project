FROM ruby:2.4-alpine
# throw errors if Gemfile has been modified since Gemfile.lock
RUN bundle config --global frozen 1

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY Gemfile /usr/src/app/
COPY Gemfile.lock /usr/src/app/
RUN apk add --update \
  build-base \
  libxml2-dev \
  libxslt-dev \
  && rm -rf /var/cache/apk/*
RUN bundle install

COPY . /usr/src/app/
CMD ["ruby", "./check.rb"]