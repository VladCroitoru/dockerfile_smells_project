FROM ruby:2.3.0

VOLUME data
EXPOSE 9292

RUN mkdir -p /app/views
COPY views /app/views
WORKDIR /app
COPY Gemfile .
COPY config.ru .

RUN bundle install

ENTRYPOINT ["rackup", "--host", "0.0.0.0"]
