FROM ruby:2.3

RUN mkdir /app
WORKDIR /app

COPY Gemfile* /app/
RUN bundle install

COPY . /app

EXPOSE 3000
CMD puma -C config/puma.rb
