FROM ruby:2.6 as build

RUN gem install bundler

WORKDIR /app

COPY gems.* /app/
RUN bundle install

FROM ruby:2.6-alpine

WORKDIR /app

COPY --from=build /usr/local/bundle/ /usr/local/bundle/
COPY gems.* /app/
COPY *.rb /app/
COPY src/*.rb /app/src/

CMD ["ruby", "main.rb"]
