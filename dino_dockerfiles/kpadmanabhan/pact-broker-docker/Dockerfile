FROM ruby

MAINTAINER Karthik Padmanabhan <@humblelistener>

RUN mkdir -p /usr/local/pact_broker

COPY . /usr/local/pact_broker

RUN chmod +x -R /usr/local/pact_broker

WORKDIR /usr/local/pact_broker

RUN bundle install

EXPOSE 9292

ENTRYPOINT bundle exec rackup -p 9292 -o 0.0.0.0 /usr/local/pact_broker/config.ru
