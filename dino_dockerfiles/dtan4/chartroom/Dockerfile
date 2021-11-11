FROM ruby:2.3.0
MAINTAINER Daisuke Fujita <dtanshi45@gmail.com> (@dtan4)

RUN bundle config --global frozen 1

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD Gemfile /usr/src/app/
ADD Gemfile.lock /usr/src/app/
RUN bundle install --without test development --system

ADD . /usr/src/app

RUN apt-get update && apt-get install -y nodejs --no-install-recommends && rm -rf /var/lib/apt/lists/*

ENV RACK_ENV production
EXPOSE 9292

CMD ["bundle", "exec", "rackup", "-p", "9292"]
