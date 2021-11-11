FROM ruby:2.3-slim

MAINTAINER developers@forward3d.com

RUN apt-get update
WORKDIR /opt/frugal
COPY Gemfile /opt/frugal/Gemfile
COPY Gemfile.lock /opt/frugal/Gemfile.lock

RUN \
  apt-get install -y build-essential && \
  bundle install --without development && \
  apt-get remove -y build-essential && \
  apt-get autoremove -y && apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY . /opt/frugal

# Entrypoint is to run the frugal binary
ENTRYPOINT ["/usr/local/bin/ruby", "/opt/frugal/bin/check"]
