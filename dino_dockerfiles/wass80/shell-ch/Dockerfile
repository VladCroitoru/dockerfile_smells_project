FROM ruby:2.3

RUN apt-get update -y && apt-get install -y zsh

RUN mkdir -p /tmp/shell
WORKDIR /tmp/shell

ADD Gemfile ./
RUN bundle install

ADD start.sh ./
RUN chmod +x start.sh

ADD bot.rb ./

ENV LANG C.UTF-8
