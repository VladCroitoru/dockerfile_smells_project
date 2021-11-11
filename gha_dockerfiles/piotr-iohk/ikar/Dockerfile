FROM ruby:2.7.1-alpine

RUN apk add --update build-base libffi-dev

ENV APP_HOME /app
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

ADD Gemfile* $APP_HOME/
RUN bundle config set without 'development test'
RUN bundle install

ADD . $APP_HOME

CMD ["ruby", "app.rb"]
