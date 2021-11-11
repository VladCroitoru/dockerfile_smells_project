FROM ruby:2.3

RUN mkdir /gustos_ms
WORKDIR /gustos_ms

ADD Gemfile /gustos_ms/Gemfile
ADD Gemfile.lock /gustos_ms/Gemfile.lock

RUN bundle install
ADD . /gustos_ms

EXPOSE 4006