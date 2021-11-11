FROM ruby:2.3

RUN mkdir /laboratorio1
WORKDIR /laboratorio1

ADD Gemfile /laboratorio1/Gemfile
ADD Gemfile.lock /laboratorio1/Gemfile.lock

RUN bundle install
ADD . /laboratorio1
