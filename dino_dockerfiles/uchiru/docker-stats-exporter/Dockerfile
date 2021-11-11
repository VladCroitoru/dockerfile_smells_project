FROM ruby:2.3.3

ENV APP_ENV production
RUN mkdir -p /app
WORKDIR /app

COPY Gemfile /app
COPY Gemfile.lock /app
RUN bundle install

COPY . /app

EXPOSE 3120

CMD ["rackup"]
