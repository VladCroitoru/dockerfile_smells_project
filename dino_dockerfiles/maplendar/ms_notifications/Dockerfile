FROM ruby:2.4.2
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs
ENV ms-notifications /notifications
RUN mkdir /ms-notifications
WORKDIR /ms-notifications
COPY . /ms-notifications
ADD Gemfile /ms-notifications/Gemfile
ADD Gemfile.lock /ms-notifications/Gemfile.lock
RUN bundle install
EXPOSE  4003 27017
ADD . /ms-notifications
