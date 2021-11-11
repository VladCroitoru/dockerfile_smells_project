
FROM ruby:2.1

MAINTAINER Kai Heikka <synomi66@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y build-essential libpq-dev git

WORKDIR /app/

#thingspeak setup
RUN git clone https://github.com/yuzhangiot/thingspeak.git
WORKDIR /app/thingspeak/
RUN bundle install

#db example
ADD database.yml.example config/database.yml

EXPOSE 80

CMD bundle exec rails server -p 80
