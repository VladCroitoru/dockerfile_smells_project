FROM ruby:2.7

RUN mkdir /app
WORKDIR /app

COPY .ruby-version Gemfile Gemfile.lock /app/
RUN bundle install

ADD . /app

CMD ["rails", "server", "-b", "0.0.0.0"]
