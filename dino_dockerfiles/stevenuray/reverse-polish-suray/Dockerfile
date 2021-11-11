FROM ruby:2.4.1

RUN mkdir /app
WORKDIR /app
ADD . /app

RUN bundle install

RUN rspec

WORKDIR /app/bin

ENTRYPOINT [ "ruby", "rpn_suray" ]
