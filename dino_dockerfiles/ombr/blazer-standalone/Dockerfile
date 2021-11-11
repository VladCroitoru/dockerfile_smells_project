FROM ruby:2.4.1
MAINTAINER Luc Boissaye <luc@boissaye.fr>

RUN gem install bundler
RUN bundle config --global silence_root_warning 1

WORKDIR /var/app

COPY Gemfile /var/app
COPY Gemfile.lock /var/app
RUN bundle install

COPY . /var/app

EXPOSE 5000

CMD rails s -p 5000 -b 0.0.0.0
