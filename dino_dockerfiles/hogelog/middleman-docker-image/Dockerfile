FROM ruby:2.3.3

RUN apt-get update -qq && apt-get install -y build-essential 

RUN apt-get install -y nodejs rsync

ADD Gemfile /tmp/Gemfile
ADD Gemfile.lock /tmp/Gemfile.lock
RUN cd /tmp && bundle install -j5
