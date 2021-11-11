FROM ruby:2.2.3
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs
ADD . /app
WORKDIR /app
RUN bundle install
CMD ["bundle","exec","rails","s","-p","3000","-b","0.0.0.0"]
