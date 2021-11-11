FROM ruby:2.5.1
RUN apt-get update -qq && apt-get install -y build-essential
RUN mkdir /app
RUN curl -sL https://deb.nodesource.com/setup_11.x | bash -
RUN apt-get install -y nodejs
RUN curl https://cli-assets.heroku.com/install.sh | sh
WORKDIR /app
COPY Gemfile /app/Gemfile
COPY Gemfile.lock /app/Gemfile.lock
RUN bundle install
COPY . /app