FROM ruby:2.3.0
MAINTAINER Daisuke Fujita <dtanshi45@gmail.com> (@dtan4)

RUN bundle config --global frozen 1

RUN apt-get update && \
    apt-get install -y nodejs --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY Gemfile /usr/src/app/
COPY Gemfile.lock /usr/src/app/

RUN bundle install --without test development -j4

COPY . /usr/src/app

ENV RAILS_ENV production

EXPOSE 5000

ENTRYPOINT ["bin/docker-entrypoint.sh"]
