FROM ruby:2.3

RUN mkdir /grades_ms
WORKDIR /grades_ms

ADD Gemfile /grades_ms/Gemfile
ADD Gemfile.lock /grades_ms/Gemfile.lock

RUN bundle install
ADD . /grades_ms

expose 4002
