FROM ruby:2.7.2

RUN apt-get update && apt-get install -y nodejs yarn postgresql-client

RUN mkdir /app
WORKDIR /app
COPY Gemfile Gemfile.lock ./
RUN gem install bundler
RUN bundle install
COPY . .

EXPOSE 3000
CMD ["rails", "server", "-b", "0.0.0.0"]
