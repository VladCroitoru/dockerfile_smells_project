FROM ruby:3.0.2

RUN curl -sL https://deb.nodesource.com/setup_12.x | bash - && apt-get update && \
    apt-get install -y nodejs --no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN apt-get update -qq && apt-get install -y build-essential libpq-dev sudo vim

RUN apt-get update && apt-get install -y curl apt-transport-https wget && \
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
    apt-get update && apt-get install -y yarn && apt-get install imagemagick


RUN yarn add node-sass

WORKDIR /app
COPY Gemfile .
COPY Gemfile.lock .
COPY yarn.lock .
COPY package.json .
RUN bundle install

RUN yarn install
COPY . /app

# RUN rails webpacker:install
RUN NODE_ENV=production ./bin/webpack

EXPOSE 3000