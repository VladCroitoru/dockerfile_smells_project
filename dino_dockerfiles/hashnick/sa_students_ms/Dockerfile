FROM ruby:2.4

RUN mkdir /sa_students_ms
WORKDIR /sa_students_ms

ADD Gemfile /sa_students_ms/Gemfile
ADD Gemfile.lock /sa_students_ms/Gemfile.lock

RUN bundle install
ADD . /sa_students_ms

EXPOSE 4000