FROM ruby:2.1.6

ENV APP_HOME /sidekiq-pusher

RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

ADD Gemfile* $APP_HOME/
RUN bundle install

ADD . $APP_HOME