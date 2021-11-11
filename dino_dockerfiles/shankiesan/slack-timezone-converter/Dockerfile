FROM ruby:2.3.3

ADD ./app /app

WORKDIR /app

RUN bundle install

EXPOSE 443
EXPOSE 80

CMD ruby slack-timezone-converter.rb $SLACK_TOKEN