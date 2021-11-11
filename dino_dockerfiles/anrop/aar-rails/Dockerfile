FROM ruby:2.6.6-alpine
RUN apk add --no-cache --update build-base postgresql-dev tzdata
RUN mkdir /aar-rails
WORKDIR /aar-rails
ADD Gemfile /aar-rails/Gemfile
ADD Gemfile.lock /aar-rails/Gemfile.lock
RUN bundle install -j4
ADD . /aar-rails
CMD rm -f tmp/pids/server.pid && rails server -b '0.0.0.0'
