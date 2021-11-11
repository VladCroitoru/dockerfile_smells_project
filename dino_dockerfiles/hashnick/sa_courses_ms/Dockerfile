FROM ruby:2.3

RUN mkdir /sa_courses_ms
WORKDIR /sa_courses_ms

ADD Gemfile /sa_courses_ms/Gemfile
ADD Gemfile.lock /sa_courses_ms/Gemfile.lock

RUN bundle install
ADD . /sa_courses_ms

EXPOSE 4001