FROM ruby:3.0.1-alpine

WORKDIR /app

ENV RAILS_ENV development

COPY . .
RUN apk update \
 && apk upgrade \
 && apk add \
    build-base \
    tzdata \
    libxml2-dev \
    libxslt-dev \
    postgresql-client \
    postgresql-dev
RUN bundle install
ONBUILD rails db:setup
