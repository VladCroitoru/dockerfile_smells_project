FROM ruby:3.0.2-alpine3.14

RUN apk update && apk add --no-cache \
    libxml2-dev \
    curl-dev \
    make \
    gcc \
    g++ \
    git \
    libc-dev \
    mysql-client \
    mysql-dev \
    tzdata \
    zsh \
    vim

RUN mkdir -p /Short-Diary

ENV APP_ROOT /Short-Diary

WORKDIR $APP_ROOT

COPY Gemfile $APP_ROOT/Gemfile
COPY Gemfile.lock $APP_ROOT/Gemfile.lock

RUN gem install bundler && \
    bundle install

COPY . $APP_ROOT
RUN mkdir -p tmp/sockets tmp/pids log

EXPOSE 3001