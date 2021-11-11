FROM ruby:2.4.0-slim
MAINTAINER gill@createk.io

RUN apt-get update && apt-get install -y \
  build-essential \
  nodejs \
  libmysqlclient-dev && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir -p /app
WORKDIR /app

COPY Gemfile Gemfile.lock ./
RUN gem install bundler && bundle install

COPY . ./

EXPOSE 3000
