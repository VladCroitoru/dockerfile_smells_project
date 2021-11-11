FROM ruby:2.4.1-slim
MAINTAINER me@juntaki.com

RUN apt-get update && apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN apt-get update
RUN apt-get install -y build-essential \
    libsqlite3-dev \
    nodejs \
    yarn \
    ffmpegthumbnailer \
    git

RUN mkdir -p /app
WORKDIR /app

COPY Gemfile Gemfile.lock ./
RUN gem install bundler && bundle install --jobs 20 --retry 5 --without development

COPY package.json yarn.lock ./
RUN yarn

COPY . ./

EXPOSE 3000
WORKDIR /app
VOLUME /app/files
VOLUME /app/log

ENV RAILS_ENV production
RUN rails assets:precompile
RUN rails db:migrate
CMD rails s -b 0.0.0.0
