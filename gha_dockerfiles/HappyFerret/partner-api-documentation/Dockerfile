FROM ruby:2.6.5

RUN apt-get update && apt-get install -y nodejs \
&& apt-get clean && rm -rf /var/lib/apt/lists/*

ADD ./Gemfile ./Gemfile.lock /app/
WORKDIR /app

RUN gem install bundler --version '2.0.2'
RUN bundle install

COPY . /app
