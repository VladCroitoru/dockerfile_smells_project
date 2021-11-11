FROM ruby:2.1.3

RUN mkdir /app
WORKDIR /app

ADD Gemfile /app/Gemfile
ADD Gemfile.lock /app/Gemfile.lock

RUN bundle install --system

ADD . /app

EXPOSE 3000

CMD rackup -p 3000
