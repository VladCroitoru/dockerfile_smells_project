FROM ruby:3.0.1-alpine3.13

WORKDIR /parser-manager

RUN apk --no-cache add \
    build-base \
    poppler-utils \
    postgresql-dev \
    shared-mime-info

COPY Gemfile Gemfile.lock ./

RUN gem update --system \
    && gem install bundler -v 2.2.15 \
    && bundle install

COPY . .
