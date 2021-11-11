FROM ubuntu:trusty
MAINTAINER Guillaume Carre <guillaume.carre@ticketfly.com>

RUN apt-get update &&\
    apt-get install -y bundler git &&\
    apt-get install -y mongodb

ADD . /pagerbot
WORKDIR /pagerbot

RUN	bundle install
RUN mkdir -p /data/db/
RUN chmod +x run.sh

EXPOSE 4567

CMD ["/pagerbot/run.sh"]
