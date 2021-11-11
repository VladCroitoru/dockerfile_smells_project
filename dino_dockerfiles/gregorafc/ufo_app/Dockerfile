FROM ruby:2.3.3

MAINTAINER gregor.afc@gmail.com

RUN apt-get update -qq && apt-get install -y build-essential

RUN apt-get install -y node.js

RUN mkdir /ufo_app

COPY . /ufo_app

WORKDIR /ufo_app

RUN bundle install

RUN bundle exec rake db:migrate

EXPOSE 3000

CMD bin/rails server --port 3000 --binding 0.0.0.0