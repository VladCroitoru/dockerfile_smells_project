FROM ruby:2.3.1-alpine

RUN gem install term-ansicolor

RUN mkdir /app
WORKDIR /app
ADD . /app

CMD ruby statsd.rb
