FROM ubuntu:trusty
MAINTAINER Guillaume Carre <guillaume.carre@ticketfly.com>

RUN apt-get update && apt-get install -y bundler

ADD . /jirabot
WORKDIR /jirabot

RUN apt-get install -y libssl-dev

RUN	bundle install

CMD ["foreman", "start"]
