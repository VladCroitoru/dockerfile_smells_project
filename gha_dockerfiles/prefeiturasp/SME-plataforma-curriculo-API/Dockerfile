FROM ruby:2.5.1-stretch

ENV LANG en_US.UTF-8 
ENV LANGUAGE en_US:en 
ENV LC_ALL en_US.UTF-8

RUN mkdir -p /app 
WORKDIR /app

RUN apt-get update -y && apt-get upgrade -y && update-ca-certificates --fresh
RUN curl -fsSL https://deb.nodesource.com/setup_8.x | sh

RUN apt-get install -y \
    build-essential \
    git \
    imagemagick \
    libxml2-dev \
    libxslt-dev \
    nodejs \
    libpq-dev \
    tzdata \
    libyaml-dev \
    zlib1g-dev

RUN npm install -g yarn
RUN yarn install

COPY Gemfile Gemfile.lock ./

RUN gem install bundler
RUN bundle install --jobs 20 --retry 5

COPY . ./
EXPOSE 8666


CMD bundle exec rake db:migrate && bundle exec puma -v -C config/puma.rb
