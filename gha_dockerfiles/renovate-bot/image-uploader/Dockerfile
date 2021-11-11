FROM ruby:2.4
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev imagemagick nodejs
RUN mkdir /myapp
WORKDIR /myapp
COPY Gemfile /myapp/Gemfile
COPY Gemfile.lock /myapp/Gemfile.lock
RUN bundle install
COPY . /myapp
RUN cd /myapp && rake assets:precompile