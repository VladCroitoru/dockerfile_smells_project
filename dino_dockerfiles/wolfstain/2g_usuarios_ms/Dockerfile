FROM ruby:2.3

RUN mkdir /users-ms
WORKDIR /users-ms

ADD Gemfile /users-ms/Gemfile
ADD Gemfile.lock /users-ms/Gemfile.lock

RUN bundle install
ADD . /users-ms

EXPOSE 4001
