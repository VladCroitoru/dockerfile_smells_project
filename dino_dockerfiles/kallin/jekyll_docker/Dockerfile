FROM ruby:2.2
MAINTAINER kallin.nagelberg@gmail.com

RUN mkdir /opt/jekyll

WORKDIR /opt/jekyll

ADD Gemfile ./

RUN gem install bundler

RUN bundle install

RUN curl -sL https://deb.nodesource.com/setup_5.x | bash -

RUN apt-get install --yes nodejs