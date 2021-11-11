FROM ruby:2.2.0
MAINTAINER Francis <francis.tm@gmail.com>

RUN mkdir -p /opt/scripts
COPY scripts /opt/scripts/yiichina-sign

WORKDIR /opt/scripts/yiichina-sign
RUN bundle install
CMD bundle exec ruby ./autosign.rb
